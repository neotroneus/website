from django.db import models

class Website(models.Model):
    description = models.CharField(max_length=200)
    image = models.FileField()

    def __str__(self):
        return self.description