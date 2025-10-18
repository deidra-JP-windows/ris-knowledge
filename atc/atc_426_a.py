# ある OS のバージョンは古い順に "Ocelot", "Serval", "Lynx"
# バージョン X がバージョン Y 以降のバージョンであるか判定
# バージョン X 自身もバージョン X 以降のバージョンであるものとします。

def main():
    verX, verY = map(str,input().split())
    versions = ["Ocelot", "Serval", "Lynx"]
    if versions.index(verX) >= versions.index(verY):
        print("Yes")
    else:
        print("No")
main()
