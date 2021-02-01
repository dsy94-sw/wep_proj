from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField('NAME', max_length=50)

    def __str__(self):
        return self.name