from tabnanny import verbose
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


class State(models.TextChoices):
    PROVINCE_NO_1 = _("Province No. 1")
    PROVINCE_No_2 = _("Province No. 2")
    BAGMATI_PROVINCE = _("Bagmati Province")
    GANDAKI_PROVINCE = _("Gandaki Province")
    LUMBINI_PROVINCE = _("Lumbini Province")
    KARNALI_PROVINCE = _("Karnali Province")
    SUDUR_PASCHIM_PROVINCE = _("Sudur-Paschim Province")


class District(models.TextChoices):
    BHOJPUR = _("Bhojpur")
    DHANKUTA = _("Dhankutca")
    ILAM = _("Ilam")
    JHAPA = _("Jhapa")
    KHOTANG = _("Khotang")
    MORANG = _("Morang")
    OKHALDHUNGA = _("Okhaldhunga")
    PANCHTHAR = _("Panchthar")
    SANKHUWASABHA = _("Sankhuwasabha")
    SOLUKHUMBU = _("Solukhumbu")
    SUNSARI = _("Sunsari")
    TAPLEJUNG = _("Taplejung")
    TERHATHUM = _("Terhathum")
    UDAYAPUR = _("Udayapur")
    BARA = _("Bara")
    DHANUSA = _("Dhanusa")
    MAHOTTARI = _("Mahotari")
    PARSA = _("Parsa")
    RAUTAHAT = _("Rautahat")
    SAPTARI = _("Saptari")
    SARLAHI = _("Sarlahi")
    SIRAHA = _("Siraha")
    BHAKTAPUR = _("Bhaktapur")
    CHITWAN = _("Chitwan")
    DHADING = _("Dhading")
    DOLAKHA = _("Dolakha")
    KATHMANDU = _("Kathmandu")
    KAVREPALANCHOK = _("Kavrepalanchok")
    LALITPUR = _("Lalitpur")
    MAKAWANPUR = _("Makawanpur")
    NUWAKOT = _("Nuwakot")
    RAMECHHAP = _("Ramechhap")
    RASUWA = _("Rasuwa")
    SINDHULI = _("Sindhuli")
    SINDHUPALCHOK = _("Sindhupalchowk")
    BAGLUNG = _("Baglung")
    GORKHA = _("Gorkha")
    KASKI = _("Kaski")
    LAMJUNG = _("Lamjung")
    MANANG = _("Manang")
    MUSTANG = _("Mustang")
    MYAGDI = _("Myagdi")
    NAWALPUR = _("Nawalpur")
    PARBAT = _("Parbat")
    SYANGJA = _("Syandi")
    TANAHU = _("Tanahu")
    ARGHAKHANCHI = _("Argakhanchi")
    BANKE = _("Banke")
    BARDIYA = _("Bardiya")
    DANG = _("Dang")
    GULMI = _("Gulmi")
    KAPILVASTU = _("Kapilvastu")
    PARASI = _("Parasi")
    PALPA = _("Palpa")
    PYUTHAN = _("Pyuthan")
    ROLPA = _("Rolpa")
    RUKUM = _("Rukum")
    RUPANDEHI = _("Rupandehi")
    DAILEKH = _("Dailekh")
    DOLPA = _("Dolpa")
    HUMLA = _("Humla")
    JAJARKOT = _("Jajarkot")
    JUMLA = _("Jumla")
    KALIKOT = _("Kalikot")
    MUGU = _("Mugu")
    RUKUM_PASCHIM = _("Rukum Paschim")
    SALYAN = _("Salyan")
    SURKHET = _("Surkhet")
    ACHHAM = _("Achham")
    BAITADI = _("Baitadi")
    BAJHANG = _("Bajhang")
    BAJURA = _("Bajura")
    DADELDHURA = _("Dadeldhura")
    DARCHULA = _("Darchula")
    DOTI = _("Doti")
    KAILALI = _("Kailali")
    KANCHANPUR = _("Kanchanpur")


class Gender(models.TextChoices):
    MALE = _("Male")
    FEMALE = _("Female")
    OTHER = _("Other")


class Customer(models.Model):
    citizenship_no = models.CharField(_("citizenship number"), max_length=50, unique=True)
    pan_no = models.CharField(_("pan number"), max_length=50, blank=True, default="None")
    fullname = models.CharField(_("full name"), max_length=200)
    dob = models.DateField(_("date of birth"), auto_now=False, auto_now_add=False)
    gender = models.CharField(_("gender"), max_length=6, choices=Gender.choices)
    email = models.EmailField(_("email"), max_length=254)
    phone = models.CharField(_("phone number"), max_length=50)
    occupation = models.CharField(_("occupation"), max_length=200)
    city = models.CharField(_("town/city"), max_length=200)
    district = models.CharField(_("district"), max_length=40, choices=District.choices)
    state = models.CharField(_("state"), max_length=40, choices=State.choices)
    country = models.CharField(
        _("country"), max_length=100, default="Nepal", blank=True
    )
    address = models.TextField(_("address"), max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.fullname

    def get_absolute_url(self):
        return reverse("customer-detail", kwargs={"id": self.id})

