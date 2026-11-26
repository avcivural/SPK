# SPK Düzey 1 Çalışma

Tek sayfalık, sunucusuz çalışma uygulaması (SPK/SPL Düzey 1: 1001, 1003, 1005, 1012).

## Yayınlama (GitHub Pages)
1. Bu klasörün tamamını bir GitHub deposuna yükle.
2. Depo → Settings → Pages → Source: "Deploy from a branch", Branch: `main`, klasör: `/docs`.
3. Birkaç dakika sonra `https://<kullanici>.github.io/<depo>/` adresinde açılır.

## Veri güncelleme
- Bölümler `data/bolumler/*.json` içindedir. Değişiklikten sonra:
  `python3 tools/dogrula.py data/bolumler` (şema kontrolü) ve `python3 tools/build.py` (docs/veri.js üretir).
- `docs/veri.js` üretilmiş dosyadır; elle düzenlenmez.

## Notlar
- Sorular SPL sınavlarından alınmamıştır; mevzuat metinlerinden özgün hazırlanmıştır.
- Her bölümün `dogrulama_notlari` alanı, resmi metinle teyit edilmesi gereken noktaları listeler.
