import json,pytest
from launcher.discovery import find_installation
def test_finds(tmp_path):
    game=tmp_path/".minecraft"; d=game/"versions"/"1.12.2-forge-14.23.5.2860"; d.mkdir(parents=True)
    data={"id":d.name,"inheritsFrom":"1.12.2","mainClass":"net.minecraft.launchwrapper.Launch"}
    (d/(d.name+".json")).write_text(json.dumps(data))
    x=find_installation(tmp_path); assert x.version_id==d.name and x.game_dir==game.resolve()
def test_missing(tmp_path):
    with pytest.raises(ValueError): find_installation(tmp_path)
