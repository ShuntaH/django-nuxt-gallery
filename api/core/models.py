from django.db import models

# Create your models here.


class Photos(models.Model):
    name = models.CharField(max_length=120)
    picture = models.FileField()
    description = models.TextField()

    def __str_(self):
        return "{} information".format(self.name)
