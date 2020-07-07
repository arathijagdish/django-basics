from django.db import models
from category.models import Category, SubCategory

# Create your models here.
class Course(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Title',
        unique=True
    )
    video_link=models.URLField(
        max_length=1024,
        unique=True,
        verbose_name='Video Link'
    )
    category=models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE
    )
    subcategory = models.ForeignKey(
        to='category.SubCategory',
        on_delete=models.PROTECT,
    )
    created_on=models.DateField(
        auto_now_add=True,
    )
    last_updated=models.DateField(
        auto_now=True,
    )