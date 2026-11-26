# Veri şeması (bölüm dosyası: data/bolumler/<bolum-id>.json)

```json
{
  "id": "1001-1.2.1",
  "ders": "1001",
  "ad": "Özel Durumlar Tebliği II-15.1",
  "kaynaklar": [
    {"ad": "Özel Durumlar Tebliği (II-15.1)", "url": "...", "erisim_tarihi": "2026-11-25"}
  ],
  "sunum": [
    {"baslik": "...", "metin": "kısa, kendi cümlelerimizle", "dayanak": "md. X"}
  ],
  "kartlar": [
    {"on": "kavram / soru", "arka": "kural / cevap", "dayanak": "md. X"}
  ],
  "sorular": [
    {
      "id": "1001-1.2.1-01",
      "kok": "soru kökü",
      "siklar": {"A": "", "B": "", "C": "", "D": "", "E": ""},
      "dogru": "C",
      "gerekce": "1-2 cümle: neden doğru",
      "tuzak": {"A": "neden yanlış", "B": "..."},
      "dayanak": "md. X",
      "zorluk": 1,
      "tip": "kavram | kural | sayi | hesap | karsilastirma"
    }
  ]
}
```

Kurallar
- Her sorunun tek doğru şıkkı, bir dayanağı ve bir gerekçesi olur.
- Sayı, süre, oran içeren sorularda dayanak maddesi resmi metinden doğrulanır.
- Hesap soruları kodla doğrulanır.
- Sunum ve kart metinleri SPL kitabından kopyalanmaz; resmi mevzuat esas alınır, kendi cümlelerimizle yazılır.
- Bölüm sonu seti: 10 soru. Deneme havuzu ayrı dosyada (data/deneme/<ders>.json), ders başına en az 75 soru.
