from operator import truediv
from django.db import models

# Create your models here.



class Contacts(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100 , blank=True,null=True)
    email = models.EmailField(null=True, blank=True)
    relationship = models.CharField(max_length=100, blank=True, null=True )
    number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.TextField(blank=True,null=True)




    def __str__(self):
        return self.first_name  