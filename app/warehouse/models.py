from django.db import models
from django.db.models.deletion import RESTRICT


class Time_Dim(models.Model):
    year = models.PositiveSmallIntegerField()
    month = models.PositiveSmallIntegerField()
    day = models.PositiveSmallIntegerField()
    day_of_week = models.PositiveSmallIntegerField()


class Purchase_Record_Dim(models.Model):
    purchase_id = models.BigIntegerField(verbose_name="Purchase Id")
    invoice_no = models.CharField(verbose_name="Invoice Number", max_length=50)
    vendor_name = models.CharField(verbose_name="Vendor Name", max_length=200)
    vendor_address = models.CharField(verbose_name="Vendor Address", max_length=300)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['purchase_id'], name="UniquePurchaseId")
        ]


class Customer_Dim(models.Model):
    customer_id = models.BigIntegerField(verbose_name="Customer Id")
    citizenship_no = models.CharField(verbose_name="Citizenship Number", max_length=50)
    pan_no = models.CharField(verbose_name="PAN Number", max_length=50)
    first_name = models.CharField(verbose_name="First Name", max_length=200)
    middle_name = models.CharField(verbose_name="Middle Name", max_length=200)
    surname = models.CharField(max_length=200)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=5)
    phone = models.CharField(max_length=15)
    dob = models.DateField(verbose_name="Date of Birth")
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.TextField(max_length=500)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['citizenship_no'], name="UniqueCitizenship"),
            models.UniqueConstraint(fields=['pan_no'], name="UniquePAN"),
        ]  


class Scheme_Dim(models.Model):
    scheme_id = models.BigIntegerField(verbose_name="Scheme Id")
    scheme_name = models.CharField(verbose_name="Scheme Name", max_length=300)
    description = models.CharField(max_length=500)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['scheme_id'], name="UniqueSchemeId"),
        ]


class Sale_Record_Dim(models.Model):
    sale_id = models.BigIntegerField(verbose_name="Sale Id")
    invoice_no = models.CharField(verbose_name="Invoice Number", max_length=50, blank=True, default="None")
    dc_no = models.CharField(verbose_name="Delivery Challan No.", max_length=50, blank=True, default="None")
    payment_mode = models.CharField(verbose_name="Payment Mode", max_length=50, blank=True, default="None")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['sale_id'], name="UniqueSaleId"),
        ]


class Vehicle_Dim(models.Model):
    vehicle_id = models.BigIntegerField(verbose_name="Vehicle Id")
    vehicle_model = models.CharField(verbose_name="Vehicle Model", max_length=100)
    color =  models.CharField(max_length=100)
    chasis_no =  models.CharField(verbose_name="Chasis Number", max_length=100)
    engine_no =  models.CharField(verbose_name="Engine Number", max_length=100)
    reg_no = models.CharField(verbose_name="Registration Number", max_length=100)
    key_no =  models.CharField(verbose_name="Key Number", max_length=20)
    battery_no =  models.CharField(verbose_name="Battery Number", max_length=100)
    purchase_price = models.DecimalField(verbose_name="Purchase Price", max_digits=10, decimal_places=2)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['chasis_no', 'engine_no'], name="UniqueChasisEngine"),
            models.UniqueConstraint(fields=['reg_no'], name="UniqueVehicleRegistration"),
            models.UniqueConstraint(fields=['vehicle_id'], name="UniqueVehicleId"),
        ]


class Sale_Fact(models.Model):
    time_key = models.ForeignKey(to=Time_Dim, on_delete=RESTRICT)
    customer_key = models.ForeignKey(to=Customer_Dim, on_delete=RESTRICT)
    vehicle_key = models.ForeignKey(to=Vehicle_Dim, on_delete=RESTRICT)
    purchase_record_key = models.ForeignKey(to=Purchase_Record_Dim, on_delete=models.RESTRICT )
    sale_record_key = models.ForeignKey(to=Sale_Record_Dim, on_delete=RESTRICT)
    scheme_key = models.ForeignKey(to=Scheme_Dim, on_delete=RESTRICT)
    purchase_amount = models.DecimalField(verbose_name="Purchase Amount", max_digits=10, decimal_places=2)
    sale_amount = models.DecimalField(verbose_name="Sale Amount", max_digits=10, decimal_places=2)
    revenue = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    finance_amount = models.DecimalField(verbose_name="Finance Amount", max_digits=10, decimal_places=2)
    exchange_amount = models.DecimalField(verbose_name="Exchange Amount", max_digits=10, decimal_places=2)

