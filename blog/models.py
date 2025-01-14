from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='category_icons/')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = 'Categories'
