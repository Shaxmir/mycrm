from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission



class User(AbstractUser):
    # Новые поля профиля
    photo = models.ImageField(upload_to='users/photos/', null=True, blank=True)
    first_name = models.CharField(max_length=150)  # уже есть в AbstractUser, но можно переопределить verbose_name
    last_name = models.CharField(max_length=150)   # тоже есть в AbstractUser
    middle_name = models.CharField("Отчество", max_length=150, null=True, blank=True)
    email = models.EmailField(unique=True)  # уже есть, но можно переопределить
    phone = models.CharField("Мобильный телефон", max_length=20, blank=True, null=True)
    birth_date = models.DateField("День рождения", null=True, blank=True)
    department = models.CharField("Подразделение", max_length=100, null=True, blank=True)
    position = models.CharField("Должность", max_length=100, null=True, blank=True)

    role = models.CharField(
        max_length=50,
        choices=[('admin', 'Администратор'), ('manager', 'Менеджер'), ('employee', 'Сотрудник')]
    )
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',
        blank=True
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.username})"
