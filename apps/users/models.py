from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=50, choices=[('admin', 'Администратор'), ('manager', 'Менеджер'), ('employee', 'Сотрудник')])
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Название может быть любым уникальным
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',
        blank=True
    )
    def __str__(self):
        return self.username
