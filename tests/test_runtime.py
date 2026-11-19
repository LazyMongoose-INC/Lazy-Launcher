import json
from launcher.discovery import ForgeInstallation
from launcher.runtime import build_command
def test_command(tmp_path):
    g=tmp_path; (g/"versions"/"1.12.2").mkdir(parents=True); (g/"versions"/"forge").mkdir()
    lib=g/"libraries"/"net"/"minecraft"/"launchwrapper"/"1.12"; lib.mkdir(parents=True); (lib/"launchwrapper-1.12.jar").write_bytes(b"jar")
    (g/"versions"/"1.12.2"/"1.12.2.jar").write_bytes(b"jar")
    (g/"assets"/"indexes").mkdir(parents=True); (g/"assets"/"indexes"/"1.12.json").write_text("{}")
    (g/"versions"/"1.12.2"/"1.12.2.json").write_text(json.dumps({"assetIndex":{"id":"1.12"}}))
    m={"id":"forge","inheritsFrom":"1.12.2","mainClass":"net.minecraft.launchwrapper.Launch","minecraftArguments":"--username TestUser --uuid offline-id","libraries":[{"name":"net.minecraft:launchwrapper:1.12"}]}
    i=ForgeInstallation(g,"forge",g/"versions"/"forge"/"forge.json",m)
    cmd,cwd=build_command(i,"TestUser",g/"java.exe",4096)
    assert "-Xmx4096M" in cmd and "TestUser" in cmd and cwd==g.resolve()
