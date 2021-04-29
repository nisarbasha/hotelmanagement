

# Create your models here.
from django.db import models


class customer_reg_form(models.Model):
    c_name = models.CharField(max_length=50)
    c_address = models.CharField(max_length=50)
    c_mail_id = models.EmailField(max_length=50)
    c_mob_no = models.CharField(max_length=10)
    c_username = models.CharField(max_length=50)
    c_password = models.CharField(max_length=50)

    def __str__(self):
        return self.c_name

class room_booking_form(models.Model):
    name = models.CharField(max_length=50)
    no_adults = models.CharField(max_length=50)
    name_adults = models.CharField(max_length=500)
    no_child = models.CharField(max_length=50)
    name_child = models.CharField(max_length=500)
    phone_num = models.CharField(max_length=10)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    room_no = models.CharField(max_length=10)
    room_no1=models.CharField(max_length=10)

    def __str__(self):
        return self.name





class generate_bill(models.Model):
    room_no = models.CharField(max_length=10)
    b_name = models.CharField(max_length=50)
    mob_num = models.CharField(max_length=10)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    total = models.CharField(max_length=50)

    def __str__(self):
        return self.b_name


class EmployeeApi(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=225)


    def __str__(self):
        return self.username

