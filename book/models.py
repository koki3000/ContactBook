from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    birthday = models.DateField(null=True, blank=True)
    info = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name[0:25]