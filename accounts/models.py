from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField('Аватар', upload_to='accounts', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('account_detail')
