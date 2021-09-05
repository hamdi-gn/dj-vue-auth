from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
import uuid
import os

def get_file_path1(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('images/profile_images', filename)

def get_file_path2(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('images/cover_images', filename)

class UserManager(BaseUserManager):
    def create_user(self, email, username, password):
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email= email,
            username= username,
            password= password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(null=False, max_length=100,unique=True)
    username = models.CharField(max_length=10, unique=True)
    profile_image = models.ImageField(upload_to= get_file_path1, blank=True, null=True)
    cover_image = models.ImageField(upload_to= get_file_path2, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    birthday = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    profession = models.CharField(max_length=50, blank=True, null=True)
    about = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.IntegerField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    skills = models.CharField(max_length=50, blank=True, null=True)
    facebook_link = models.CharField(max_length=50, blank=True, null=True)
    twitter_link = models.CharField(max_length=50, blank=True, null=True)
    instagram_link = models.CharField(max_length=50, blank=True, null=True)
    linkedin_link = models.CharField(max_length=50, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj ):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True