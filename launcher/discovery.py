import json
from dataclasses import dataclass
from pathlib import Path
@dataclass(frozen=True)
class ForgeInstallation:
    game_dir: Path
    version_id: str
    version_json: Path
    metadata: dict
def find_installation(selected):
    root=Path(selected).expanduser().resolve()
    if not root.is_dir(): raise ValueError("Выбранная папка недоступна.")
    candidates=[root]+[root/n for n in (".minecraft","minecraft","game") if (root/n).is_dir()]
    for child in list(root.iterdir()):
        if child.is_dir(): candidates += [child/n for n in (".minecraft","minecraft") if (child/n).is_dir()]
    for game in candidates:
        versions=game/"versions"
        if not versions.is_dir(): continue
        for folder in sorted(versions.iterdir(),key=lambda p:p.name.lower(),reverse=True):
            jf=folder/(folder.name+".json")
            if not jf.is_file(): continue
            try: data=json.loads(jf.read_text(encoding="utf-8-sig"))
            except (OSError,json.JSONDecodeError): continue
            identity=(folder.name+" "+str(data.get("inheritsFrom",""))+" "+str(data.get("id",""))).lower()
            if "1.12.2" in identity and ("forge" in identity or "launchwrapper" in str(data.get("mainClass","")).lower()):
                return ForgeInstallation(game,folder.name,jf,data)
    raise ValueError("Forge для Minecraft 1.12.2 не найден. Нужна папка с versions/<forge>/<forge>.json.")
