from django.db import models

# Create your models here.
class Seller(models.Model):
    name = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=500)
    contact_no = models.CharField(max_length=10)

    def __str__(self):
        return self.name
