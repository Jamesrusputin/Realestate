from django.db import models

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    photo_main = models.ImageField(upload_to='media/%H/%M/%S/')
    photo_1 = models.ImageField(upload_to='media/%H/%M/%S/')
    photo_2 = models.ImageField(upload_to='media/%H/%M/%S/')
    photo_3 = models.ImageField(upload_to='media/%H/%M/%S/')
    is_published = models.BooleanField(default=True)
    property_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name