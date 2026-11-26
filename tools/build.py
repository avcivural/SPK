#!/usr/bin/env python3
"""data/ altındaki müfredat ve bölüm dosyalarını docs/veri.js içine gömer.
Kullanım: python3 -I tools/build.py"""
import json, os, glob

kok = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
muf = json.load(open(os.path.join(kok, "data", "mufredat.json"), encoding="utf-8"))
bolum = {}
for f in sorted(glob.glob(os.path.join(kok, "data", "bolumler", "*.json"))):
    b = json.load(open(f, encoding="utf-8"))
    bolum[b["id"]] = b

dersler = []
for d in muf["dersler"]:
    liste = []
    for x in d["bolumler"]:
        hazir = x["id"] in bolum
        liste.append({"id": x["id"], "ad": bolum[x["id"]]["ad"] if hazir else x["ad"], "hazir": hazir})
    # müfredatta listelenmeyen ama dosyası olan alt bölümleri (ör. 1003-1b) ana bölümün arkasına ekle
    for bid, b in bolum.items():
        if b["ders"] != d["kod"] or any(x["id"] == bid for x in liste):
            continue
        taban = bid.rstrip("abcdefghijklmnopqrstuvwxyz")
        idx = next((i for i, x in enumerate(liste) if x["id"] == taban), len(liste) - 1)
        while idx + 1 < len(liste) and liste[idx + 1]["id"].startswith(taban) and liste[idx + 1]["hazir"] and liste[idx + 1]["id"] < bid:
            idx += 1
        liste.insert(idx + 1, {"id": bid, "ad": b["ad"], "hazir": True})
    dersler.append({"kod": d["kod"], "ad": d["ad"], "bolumler": liste})

formul = {}
fp = os.path.join(kok, "data", "formuller.json")
if os.path.exists(fp):
    formul = json.load(open(fp, encoding="utf-8"))
veri = {"dersler": dersler, "bolumler": bolum, "format": muf["sinav_formati"], "formuller": formul, "tuzaklar": json.load(open(os.path.join(kok,"data","tuzaklar.json"),encoding="utf-8"))}
os.makedirs(os.path.join(kok, "docs"), exist_ok=True)
with open(os.path.join(kok, "docs", "veri.js"), "w", encoding="utf-8") as fh:
    fh.write("window.VERI=" + json.dumps(veri, ensure_ascii=False) + ";")
print("bölüm:", len(bolum), "| soru:", sum(len(b["sorular"]) for b in bolum.values()))
