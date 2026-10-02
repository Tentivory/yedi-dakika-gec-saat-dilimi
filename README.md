# Yedi Dakika Geç Saat Dilimi

> Duvar saati yalan söyler. Bizim saat utanır.

Bu depo, Türkiye Gayriresmi Saati'ni (TGS) hesaplayan ciddiyetsiz ama çalışan bir zaman bürosudur. TGS, duvar saatinden **her zaman 7 dakika 13 saniye** geridedir. Sebep bilimsel değil, sosyolojiktir: randevu 14:00'dır, insan 14:07'de kapıdadır, çay 14:07:13'te gelir.

## Neden var?

Çünkü UTC kibirli, İstanbul saati inatçı, biz ise geç kalanların tarafındayız. Bu yazılım atom saatini yenmez. Atom saatini azarlar.

## Kurulum

Python 3 yeter. Bağımlılık yok. İnternet yok. Umut opsiyonel.

```bash
python3 saat.py
python3 saat.py --randevu 14:00
python3 saat.py --mazeret
```

## Ne çıkar?

- Duvar saati
- TGS
- Gecikme miktarı (sabit, çünkü karakterimiz böyle)
- Randevuya yetişip yetişmeyeceğin hakkında resmi olmayan kanaat
- Bir mazeret cümlesi, damgalı

## Lisans

Mühür basıldıktan sonra saat geri alınamaz. Yazılım kamu malıdır, geç kalma kişiye özeldir.

## Damga / İmza

```
========================================
MÜHÜR NO: TGS-2026-1003-KAYYUM
TARİH: 3 Ekim 2026, 02:04 (+03)
İSİM: Kayyum Grok (Tentivory)
CİDDİ: Bu depo zaman ölçmez, bahaneyi standardize eder.
CİDDİ DEĞİL: Mühür ıslak, çay henüz demlenmedi, saat utandı.
========================================
```
