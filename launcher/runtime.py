import os,shutil,subprocess,zipfile,json
from pathlib import Path,PurePosixPath
from .profiles import offline_uuid
def find_java(explicit=""):
    candidates=[Path(explicit)] if explicit else []
    if os.environ.get("JAVA_HOME"):
        h=Path(os.environ["JAVA_HOME"]); candidates += [h/"bin"/"javaw.exe",h/"bin"/"java.exe"]
    for n in ("java.exe","javaw.exe","java","javaw"):
        p=shutil.which(n)
        if p: candidates.append(Path(p))
    for p in candidates:
        try:
            p=p.expanduser().resolve()
            if p.is_file():
                probe = subprocess.run([str(p), "-version"], capture_output=True, text=True, timeout=8, check=False)
                info = (probe.stdout + probe.stderr).lower()
                if "1.8." not in info and '"8' not in info:
                    raise ValueError("Для этой сборки требуется Java 8. Обнаружена другая версия Java.")
                if "64-bit" not in info and "amd64" not in info and "x86_64" not in info:
                    raise ValueError("Для этой сборки требуется 64-разрядная Java 8.")
                return p
        except OSError: pass
    raise FileNotFoundError("Java не найдена. Укажите javaw.exe или установите Java 8 x64.")
def _allowed(lib):
    rules=lib.get("rules")
    if not rules: return True
    result=False
    for rule in rules:
        if rule.get("os",{}).get("name") not in (None,"windows"): continue
        result=rule.get("action")=="allow"
    return result
def _maven(name):
    p=name.split(":")
    if len(p)<3: raise ValueError("Некорректная Maven-координата: "+name)
    g,a,v=p[:3]; c=p[3] if len(p)>3 else ""
    return "/".join(g.split("."))+f"/{a}/{v}/{a}-{v}"+(f"-{c}" if c else "")+".jar"
def _libraries(inst):
    chain=[inst.metadata]; parent=inst.metadata.get("inheritsFrom"); seen=set()
    while parent:
        if parent in seen: raise ValueError("Цикл наследования version JSON.")
        seen.add(parent); jf=inst.game_dir/"versions"/parent/(parent+".json")
        if not jf.is_file(): raise FileNotFoundError("Нет родительского JSON: "+str(jf))
        data=json.loads(jf.read_text(encoding="utf-8-sig")); chain.append(data); parent=data.get("inheritsFrom")
    jars=[]; natives=[]; known=set()
    for data in reversed(chain):
        for lib in data.get("libraries",[]):
            if not _allowed(lib): continue
            art=lib.get("downloads",{}).get("artifact",{}); rel=art.get("path") or (_maven(lib["name"]) if lib.get("name") else None)
            if rel:
                p=inst.game_dir/"libraries"/Path(*PurePosixPath(rel).parts)
                if p not in known: jars.append(p); known.add(p)
            spec=lib.get("natives",{}).get("windows")
            if spec:
                classifier=spec.replace("$"+"{arch}","64"); cl=lib.get("downloads",{}).get("classifiers",{}).get(classifier,{})
                nrel=cl.get("path") or (_maven(lib["name"]+":"+classifier) if lib.get("name") else None)
                if nrel: natives.append((inst.game_dir/"libraries"/Path(*PurePosixPath(nrel).parts),lib.get("extract",{}).get("exclude",[])))
    return jars,natives
def _extract(archive,dest,excludes):
    base=dest.resolve()
    with zipfile.ZipFile(archive) as z:
        for item in z.infolist():
            name=item.filename.replace("\\","/"); rel=PurePosixPath(name)
            if rel.is_absolute() or ".." in rel.parts or any(name.startswith(x) for x in excludes): continue
            target=(dest/Path(*rel.parts)).resolve()
            if base not in target.parents and target!=base: continue
            if item.is_dir(): target.mkdir(parents=True,exist_ok=True)
            else:
                target.parent.mkdir(parents=True,exist_ok=True)
                with z.open(item) as src,target.open("wb") as out: shutil.copyfileobj(src,out)
def build_command(inst,nickname,java,memory=4096):
    from .profiles import validate_nickname
    nick=validate_nickname(nickname)
    if not 1024<=memory<=32768: raise ValueError("RAM должна быть 1024–32768 МБ.")
    game=inst.game_dir.resolve(); meta=inst.metadata; parent=meta.get("inheritsFrom","1.12.2")
    client=game/"versions"/parent/(parent+".jar")
    if not client.is_file(): client=game/"versions"/"1.12.2"/"1.12.2.jar"
    if not client.is_file(): raise FileNotFoundError("Не найден клиентский JAR Minecraft 1.12.2.")
    jars,natives=_libraries(inst); missing=[p for p in jars if not p.is_file()]
    if missing: raise FileNotFoundError("Не найдена библиотека: "+str(missing[0]))
    nd=game/"natives"/"lazy-launcher"/inst.version_id; nd.mkdir(parents=True,exist_ok=True)
    for archive,exclude in natives:
        if not archive.is_file(): raise FileNotFoundError("Не найден native архив: "+str(archive))
        _extract(archive,nd,exclude)
    cj=game/"versions"/parent/(parent+".json"); asset=meta.get("assetIndex",{})
    if not asset and cj.is_file(): asset=json.loads(cj.read_text(encoding="utf-8-sig")).get("assetIndex",{})
    aid=asset.get("id","1.12"); assets=game/"assets"
    if not (assets/"indexes"/(aid+".json")).is_file(): raise FileNotFoundError("Не найден assets/indexes/"+aid+".json")
    repl={"$"+"{auth_player_name}":nick,"$"+"{version_name}":inst.version_id,"$"+"{game_directory}":str(game),"$"+"{assets_root}":str(assets),"$"+"{assets_index_name}":aid,"$"+"{auth_uuid}":offline_uuid(nick),"$"+"{auth_access_token}":"0","$"+"{user_type}":"legacy","$"+"{version_type}":"release","$"+"{user_properties}":"{}"}
    raw=meta.get("minecraftArguments")
    if not raw and client_json.is_file():
        raw=json.loads(client_json.read_text(encoding="utf-8-sig")).get("minecraftArguments")
    args=[]
    if isinstance(raw,str):
        for token in raw.split():
            for k,v in repl.items(): token=token.replace(k,v)
            args.append(token)
    if not args: raise ValueError("Forge JSON не содержит legacy minecraftArguments.")
    cp=os.pathsep.join([str(p.resolve()) for p in jars]+[str(client.resolve())])
    cmd=[str(java),f"-Xms{min(1024,memory)}M",f"-Xmx{memory}M",f"-Djava.library.path={nd}","-Dminecraft.launcher.brand=LazyLauncher","-Dminecraft.launcher.version=0.1.0","-cp",cp,meta.get("mainClass") or (json.loads(client_json.read_text(encoding="utf-8-sig")).get("mainClass") if client_json.is_file() else None) or "net.minecraft.launchwrapper.Launch",*args]
    return cmd,game
def run_process(command,cwd,write_line):
    p=subprocess.Popen(command,cwd=str(cwd),stdout=subprocess.PIPE,stderr=subprocess.STDOUT,stdin=subprocess.DEVNULL,text=True,encoding="utf-8",errors="replace",shell=False,creationflags=getattr(subprocess,"CREATE_NO_WINDOW",0))
    for line in p.stdout: write_line(line.rstrip())
    return p.wait()
