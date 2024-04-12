from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BloodBank(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=30, null=True, blank=True)
    facebook = models.URLField(max_length=300,null=True, blank=True)
    insta = models.URLField(max_length=300,null=True, blank=True)
    twitter = models.URLField(max_length=300,null=True, blank=True)
    website = models.URLField(max_length=300,null=True, blank=True)
    email = models.CharField(max_length=300,null=True, blank=True)
    phone = models.CharField(max_length=300,null=True, blank=True)
    number = models.CharField(max_length=300,null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    
    def  __str__(self):
        return self.name
    

class Blood(models.Model):
    provider = models.ForeignKey(BloodBank, on_delete=models.CASCADE)
    name =models.CharField(max_length=15)
    qty = models.IntegerField()

    def  __str__(self):
        return self.name
    

class Campaign(models.Model):
    provider = models.ForeignKey(BloodBank, on_delete=models.CASCADE)
    name =models.CharField(max_length=15)
    date = models.DateField()
    image =models.ImageField(upload_to='image')
    content =models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def  __str__(self):
        return self.name

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=30, null=True, blank=True)
    facebook = models.URLField(max_length=300,null=True, blank=True)
    insta = models.URLField(max_length=300,null=True, blank=True)
    twitter = models.URLField(max_length=300,null=True, blank=True)
    website = models.URLField(max_length=300,null=True, blank=True)
    email = models.CharField(max_length=300,null=True, blank=True)
    phone = models.CharField(max_length=300,null=True, blank=True)
    number = models.CharField(max_length=300,null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    def  __str__(self):
        return self.user.username

