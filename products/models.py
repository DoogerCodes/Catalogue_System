from django.db import models

# Create your models here.

class Items(models.Model):
    Item_Description = models.CharField(max_length=50)
    Date      = models.DateField(auto_now=False, auto_now_add=False)
    Validity  = models.BooleanField()
