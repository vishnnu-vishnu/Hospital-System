from django.db import models
import string
import random
from django.db import models

# Create your models here.

class categorydb(models.Model):
    catname=models.CharField(max_length=100 ,blank=True, null=True)
    catdes=models.CharField(max_length=300,blank=True,null=True)

class departmentdb(models.Model):
    depname=models.CharField(max_length=100,blank=True,null=True)
    depcat=models.CharField(max_length=100,null=True,blank=True)
    depdes=models.CharField(max_length=600,blank=True,null=True)
    depimg=models.ImageField(upload_to="department",null=True,blank=True)

class profiledb(models.Model):
    pname=models.CharField(max_length=100,blank=True,null=True)
    uname=models.CharField(max_length=100,blank=False,null=False)
    pmail=models.EmailField(max_length=100,blank=True,null=True)
    pmobile=models.IntegerField(max_length=100,blank=True,null=True)
    paddress=models.CharField(max_length=300,blank=True,null=True)
    pstate=models.CharField(max_length=100,blank=True,null=True)
    pimage=models.ImageField(upload_to="profileimg",blank=True,null=True)

class doctordb(models.Model):
    doctorid = models.IntegerField(unique=True)
    dname=models.CharField(max_length=100,null=True,blank=True)
    special=models.CharField(max_length=100,null=True,blank=True)
    qualification=models.CharField(max_length=100,null=True,blank=True)
    profile=models.CharField(max_length=100,null=True,blank=True)
    dmail=models.EmailField(max_length=100,null=True,blank=True)
    dphone=models.CharField(max_length=100,null=True,blank=True)
    gender=models.CharField(max_length=100,null=True,blank=True)
    fee=models.IntegerField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=8, null=True, blank=True)
    address = models.CharField(max_length=8, null=True, blank=True)
    Location = models.CharField(max_length=8, null=True, blank=True)
    Experiance = models.CharField(max_length=8, null=True, blank=True,default='Fresher')
    profileimage=models.ImageField(upload_to='profile',null=True,blank=True,default='Untitled.png')
    age=models.IntegerField(default=0,null=True,blank=True)
    dob=models.CharField(max_length=20,null=True,blank=True)
    def save(self, *args, **kwargs):
        self.dphone = str(self.dphone)

        # Check if the instance is being saved for the first time
        if not self.pk:
            # Generate a secure password
            generated_password = self.generate_password()

            # Set the password field with the plain text password
            self.password = generated_password

        # Call the original save method
        super().save(*args, **kwargs)

    def generate_password(self):
        # Customize the password generation logic here
        # For example, combining dname with some unique information
        # Include the current timestamp
        return f"{self.dname.lower()}@{self.doctorid}"

    def random_string(self, length=5):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))




