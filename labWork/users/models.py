from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    full_name = models.CharField("ФИО", max_length=150)
    phone = models.CharField("Телефон", max_length=20)
    email = models.EmailField("Email", unique=True)
    def __str__(self):
        return self.username