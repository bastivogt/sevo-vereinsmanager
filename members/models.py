from django.db import models
from django.contrib import admin

from datetime import datetime

import math

# Create your models here.

# Gender
class Gender(models.Model):
    title = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-updated_at"]


# Position
class Position(models.Model):
    title = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-updated_at"]


# Tariff
class Tariff(models.Model):
    title = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(decimal_places=2, max_digits=5)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}: {self.amount}"
    
    class Meta:
        ordering = ["-updated_at"]


# License
class License(models.Model):
    title = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-updated_at"]

# Module
class Module(models.Model):
    title = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ["-updated_at"]



# Member
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    birthday = models.DateField()
    gender = models.ForeignKey(Gender, blank=True, null=True, on_delete=models.SET_NULL)

    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)

    legal_representative = models.TextField(blank=True)

    bankname = models.CharField(max_length=255)
    iban = models.CharField(max_length=50)
    bic = models.CharField(max_length=50, blank=True)

    positions = models.ManyToManyField(Position, blank=True)
    modules = models.ManyToManyField(Module, blank=True)
    licenses = models.ManyToManyField(License, blank=True)
    tariff = models.ForeignKey(Tariff, blank=True, null=True, on_delete=models.SET_NULL)
    entry_date = models.DateField(null=True)


    chronic_diseases = models.TextField(null=True, blank=True)
    permanent_medication = models.TextField(null=True, blank=True)

    publish_fotos = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)




    @admin.display(description="Fullname")
    def get_fullname(self):
        return f"{self.firstname} {self.lastname}"
    
    @admin.display(description="Age")
    def get_age(self):
        now = datetime.now()
        b_day = datetime.strptime(str(self.birthday), "%Y-%m-%d")
        delta = now - b_day
        return math.floor(delta.days / 365)

    


    

    @admin.display(description="Modules")
    def get_modules_str(self):
        modules = self.modules.all().order_by("title")
        modules_list = [module.title for module in modules]
        return ", ".join(modules_list)
    

    @admin.display(description="Positions")
    def get_positions_str(self):
        positions = self.positions.all().order_by("title")
        positions_list = [position.title for position in positions]
        return ", ".join(positions_list)
    
    @admin.display(description="Licenses")
    def get_licenses_str(self):
        licenses = self.licenses.all().order_by("title")
        licenses_list = [license.title for license in licenses]
        return ", ".join(licenses_list)
    


    


    # def get_adult_with_child_rate(self):
    #     if self.rate.name == "Kind" and self.get_age() >= 18:
    #         return True
    #     return False
    

    def __str__(self):
        return f"{self.get_fullname()}"
    


    class Meta:
        ordering = ["-updated_at"]




