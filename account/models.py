from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class User(AbstractUser):
    profession_type = models.CharField(max_length=20)
    mobile_number = models.IntegerField()