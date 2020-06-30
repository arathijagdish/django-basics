from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(
        verbose_name = 'Author',
        blank = False,
        max_length = 100,
    )
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(
        verbose_name = 'Publisher',
        max_length = 100,
    )
    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.IntegerField(
        primary_key = True # Indicates that this is a PK
    )

    name = models.CharField(
        max_length = 100, # Required parameter
        verbose_name = "Book Name", # The text that will be displayed to the user
        unique = True,  # This filed should be unique
        blank = False, # This field cannot be left blank
    )
    
    publisher = models.ForeignKey(
        to = Publisher,
        on_delete = models.CASCADE,  
        null = True
    )

    isbn = models.CharField(
        max_length = 25, # Required parameter
        verbose_name = "ISBN", # The text that will be displayed to the user
        unique = True,  # This filed should be unique
        blank = False, # This field cannot be left blank
    )

    published_on = models.DateField(
        verbose_name = "Published on", # The text that will be displayed to the user
        blank = False, # This field cannot be left blank
        name = 'publish_date' # Name of database column
    )

    author = models.ForeignKey(
        to = Author,
        on_delete = models.CASCADE,
    )
    
    def __str__(self):
        return self.name
