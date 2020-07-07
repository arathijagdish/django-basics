from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False,
        verbose_name="Category Name",
        unique=True,
    )

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False,
        verbose_name="Sub Category",
        unique=True,
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE
    )