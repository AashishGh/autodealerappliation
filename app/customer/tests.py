from datetime import date
from django.test import TestCase
from customer.models import (
    Customer, 
    Gender,
    State,
    District,
)


class CustomerModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            citizenship_no= "1234-567-89",
            pan_no = "12345",
            fullname=  "Test Customer",
            dob = date.today(),
            gender = Gender.MALE,
            email = "testcustomer@gmail.com",
            phone = "123456789",
            occupation = "Testing",
            city = "Kathmandu",
            district = District.KATHMANDU,
            state = State.BAGMATI_PROVINCE,
            country = "Nepal",
            address = "Maitighar, Kathmandu, Nepal"
        )

    def tearDown(self):
        self.customer.delete()

    def test_customer_model_string(self):
        self.assertEqual(str(self.customer), "Test Customer")

    def test_get_absolute_url(self):
        self.assertEqual(self.customer.get_absolute_url(), f"/customers/{self.customer.id}/")

