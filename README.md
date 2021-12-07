# Ne İşe Yarıyor ?

Python ve sqlite ile yazdığım bu projede amacım insanların yabancı bir dilde bilmediği kelimeleri kayıt edebildiği bir not defteri oluşturmak.
Buna kendi oluşturduğu sözlük de diyebiliriz. Çünkü, kendi anladıkları şekilde kelimelerin anlamlarını yazabiliyorlar.
- Kelimenin tekrar eklenip eklenmediği kontrol ediliyor. Kelime eklenmiş ise **Kelime Eklenme Sayısı** arttırlıyor.
- Kulllanan kişi için istediği zaman kendi oluşturduğu kelimeler ile yapabileceği bir quiz de içermektedir. Bunun amacı kullanıcının önceden karşılaştığı kelimeleri tekrar hatırlaması ve bilme durumuna göre verilmiş puanlar ile de eksik olduğu kelimeleri görebilmesi. Kelime her sorulduğunda **Kelime Sorulma Sayısı** ve bildiğinde ise de **Doğru Bilme Sayısı** artırılıyor.
- 

|Kelime Eklenme Sayısı | Kelime Sorulma Sayısı | Doğru Bilme Sayısı| Skor|
|----------------------|-----------------------|-------------------|-----|
| 1                    |        1             |        3          |(1+1+3)/3   |

