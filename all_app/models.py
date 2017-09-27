from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime
from django.db import models

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        # Ensure that an email address is set
        if not email:
            raise ValueError('Users must have a valid e-mail address')
        # Ensure that a username is set
        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username')
        user = self.model(
            email=self.normalize_email(email),
            username=kwargs.get('username'),
           # enrichjson= enrichjson,
            FbToken = kwargs.get('FbToken'),
            TwToken = kwargs.get('TwToken'),
            SecTwToken = kwargs.get('SecTwToken'),
            InToken = kwargs.get('InToken'),
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.create_user(email, password, kwargs)
        user.is_admin = True
        user.save()

        return user

class User(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=50)
    email = models.EmailField(unique=False) #Set to False so Bot can use same email adress all over again, contact me if you want it to be set to True.
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now())
    FbToken = models.CharField(max_length=200, default='') #stavimo 200 za svaki slucaj
    TwToken = models.CharField(max_length=500, default='') #Public twitter token needed
    SecTwToken = models.CharField(max_length=500, default='') #Secret twitter token needed
    InToken = models.CharField(max_length=200, default='')
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
