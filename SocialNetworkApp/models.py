from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)
    repassword = models.CharField(max_length=50, null=True)
    dob = models.IntegerField(null=True)
    email = models.IntegerField(null=True)
    phone = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=20, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='profile')
    profile_image = models.ImageField(upload_to='avatars', default='avatars/guest.png')
    cover_image = models.ImageField(upload_to='avatars', default='avatars/cover.png')


