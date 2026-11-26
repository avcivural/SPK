import json, sys, glob
hata = 0
for yol in sorted(glob.glob(sys.argv[1] + "/*.json")):
    d = json.load(open(yol, encoding="utf-8"))
    for s in d.get("sorular", []):
        siklar = s["siklar"]
        if sorted(siklar) != list("ABCDE"):
            print("SIK HATASI", s["id"]); hata += 1
        if s["dogru"] not in siklar:
            print("DOGRU YOK", s["id"]); hata += 1
        for k in ("gerekce", "dayanak"):
            if not s.get(k):
                print("EKSIK", k, s["id"]); hata += 1
        if len(set(siklar.values())) != 5:
            print("TEKRAR SIK", s["id"]); hata += 1
    print(yol, "soru:", len(d["sorular"]), "kart:", len(d["kartlar"]), "slayt:", len(d["sunum"]))
print("HATA SAYISI:", hata)
