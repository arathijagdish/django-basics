from django.db import models

# Create your models here.
class User(models.Model):
    ROLES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    first_name = models.CharField(
        max_length=50,
        blank=True
    )
    last_name = models.CharField(
        max_length=50,
        blank=True
    )
    email = models.EmailField(
        max_length=100,
        blank=False,
        null=False,
        unique=True,
    )
    password = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        unique=True,
    )
    role = models.CharField(
        choices=ROLES,
        max_length=20,
        default='user'
    )

    def __str__(self):
        return self.email