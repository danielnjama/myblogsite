from django.db import models
from datetime import datetime



type_choices= [
    ('laptops', 'laptops'),
    ('accessories', 'accessories'),
    ('printers','printers'),
    ('phones','phones'),
    ('television','television'),
    ('repairs', 'repairs'),
    ]
class items(models.Model):
    img =models.ImageField(upload_to='photos')
    description = models.CharField(max_length=150)
    price = models.IntegerField()
    types= models.CharField(max_length=120, choices= type_choices)
    datepost = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.types
    


    class Meta:
        ordering = ['-datepost']


