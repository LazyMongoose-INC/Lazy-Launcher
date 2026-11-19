import hashlib,json,re
from pathlib import Path
NICK=re.compile(r"^[A-Za-z0-9_]{3,16}$")
def validate_nickname(value):
    value=value.strip()
    if not NICK.fullmatch(value): raise ValueError("Ник: 3–16 латинских букв, цифр или _.")
    return value
def offline_uuid(nick):
    h=hashlib.md5(("OfflinePlayer:"+validate_nickname(nick)).encode()).hexdigest()
    return f"{h[:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:]}"
def profile_path():
    p=Path.home()/"AppData"/"Roaming"/"LazyLauncher"
    if not p.parent.exists(): p=Path.home()/".config"/"LazyLauncher"
    p.mkdir(parents=True,exist_ok=True); return p/"profile.json"
def load_profile():
    defaults={"nickname":"LazyPlayer","game_dir":"","java":"","memory_mb":4096}
    try: return {**defaults,**json.loads(profile_path().read_text(encoding="utf-8"))}
    except (OSError,ValueError): return defaults
def save_profile(data):
    p=profile_path(); t=p.with_suffix(".tmp")
    t.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding="utf-8"); t.replace(p)
