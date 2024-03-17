from django.db import models

# Create your models here.

class appointmentdb(models.Model):
    bookingid=models.AutoField(primary_key=True)
    userid=models.IntegerField(null=True)
    firstname=models.CharField(max_length=50,null=True,blank=True)
    lastname=models.CharField(max_length=50,null=True,blank=True)
    email=models.EmailField(max_length=50,null=True,blank=True)
    phone=models.CharField(max_length=50,null=True,blank=True)
    department=models.CharField(max_length=50,null=True,blank=True)
    doctor=models.CharField(max_length=50,null=True,blank=True)
    date=models.DateField(max_length=50,null=True,blank=True)
    consultation=models.CharField(max_length=50,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    message=models.CharField(max_length=100,null=True,blank=True)
    age=models.CharField(max_length=100,null=True,blank=True)
    gender=models.CharField(max_length=100,null=True,blank=True)
    status=models.CharField(max_length=100,null=True,blank=True,default='Pending')
    remarks=models.CharField(max_length=200,null=True,default='No Remarks')



class contactdb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    mobile=models.IntegerField(null=True,blank=True)
    message=models.CharField(max_length=150,null=True,blank=True)
    reply=models.CharField(max_length=200,null=True,blank=True,default='NOTREPLIED')



class userdb(models.Model):
    userid=models.IntegerField(unique=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    mobile=models.IntegerField()
    password=models.CharField(max_length=15)
    address=models.CharField(max_length=50,blank=True)
    bloodgroup=models.CharField(max_length=10,blank=True)
    age=models.IntegerField(blank=True,null=True)
    sex=models.CharField(blank=True,max_length=25,null=True)
    dob=models.CharField(max_length=25,blank=True,null=True)
    profile=models.ImageField(upload_to='profile',blank=True,default='Untitled.png')



