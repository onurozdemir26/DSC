class okullar():
  def __init__(self,okulAdi,ogrenciAdi,bolumu,ders):
    self.okulAdi = okulAdi
    self.ogrenciAdi= ogrenciAdi
    self.bolumu = bolumu
    self.ders = ders



okul1=okullar("Hacettepe Üniversitesi", "Ayşe Karacı", "İletişim Bilimleri", "Reklamcılık")
okul2=okullar("Anadolu Üniversitesi","Onur Özdemir","Web Tasarım Ve Kodlama","Web Kodlama")
okul3=okullar("Orta Doğu Teknik Üniversitesi", "Eray Özdemir", "Mühendislik Fakültesi", "Gen Bilimi Mühendisiliği")

print("\nOkul: {}".format(okul1.okulAdi)+"\nÖğrenci: {}".format(okul1.ogrenciAdi)+"\nBölüm: {}".format(okul1.bolumu)+"\nDers: {} ".format(okul1.ders))
print("\nOkul: {}".format(okul2.okulAdi)+"\nÖğrenci: {}".format(okul2.ogrenciAdi)+"\nBölüm: {}".format(okul2.bolumu)+"\nDers: {} ".format(okul2.ders))
print("\nOkul: {}".format(okul3.okulAdi)+"\nÖğrenci: {}".format(okul3.ogrenciAdi)+"\nBölüm: {}".format(okul3.bolumu)+"\nDers: {} ".format(okul3.ders))