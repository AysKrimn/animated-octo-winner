from django.db import models
from apps.specuser.models import *

class FixtureGainType(models.Model):
    input = models.CharField(("Alış Type"), max_length=50)

    def __str__(self) -> str:
        return self.input


class CustomTaxRate(models.Model):
    name = models.CharField(("Verginin Adı"), max_length=50)
    rate = models.DecimalField(("Vergi Oranı (%)"), max_digits=6, decimal_places=2, unique = True)

    def __str__(self) -> str:
        return self.name


class Fixture(models.Model):
    user = models.ForeignKey(
        SiteUser, verbose_name=("Kullanıcı"), on_delete=models.CASCADE
    )
    name = models.CharField(("Demirbaş Adı"), max_length=150)
    marka = models.CharField(("Marka"), max_length=150)
    model = models.CharField(("Model"), max_length=150)
    piece = models.IntegerField(("Adet"))
    unitprice = models.DecimalField(("Birim Fiyatı"), max_digits=15, decimal_places=2)
    taxrate = models.ForeignKey(
        CustomTaxRate, to_field="rate", verbose_name=("Vergi"), on_delete=models.CASCADE
    )
    totalprice = models.DecimalField(("Toplam Fiyat"), max_digits=15, decimal_places=2)
    typeofaddition = models.ForeignKey(
        FixtureGainType, verbose_name=("Alış Şekli"), on_delete=models.CASCADE
    )
    dateofaddition = models.DateField(("Alım Tarihi"), auto_now_add=False)
    where = models.CharField(("Bulunduğu Yer"), max_length=150)
    custodian = models.CharField(("Zimmetli Kişi"), max_length=150)
    barcode = models.CharField(("Barkod Numarası"), max_length=150)
    companyName = models.CharField(("Firma Adı"), max_length=150)
    companyOfficial = models.CharField(("Firma Yetkilisi"), max_length=150)
    companyPhone = models.CharField(("Firma Telefon"), max_length=150)
    companyEmail = models.EmailField(("Firma E-Mail"), max_length=254)
    companyAddress = models.TextField(("Firma Adresi"))
    fixtureFile = models.FileField(
        ("Demirbaş Alım Belgesi"), upload_to="fixture", max_length=100
    )
    fixtureDescription = models.TextField(("Demirbaş Açıklama"), max_length=900)

    def __str__(self) -> str:
        return self.name