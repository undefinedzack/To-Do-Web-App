from django.db import models

# Create your models here.

class Text(models.Model):
    text = models.CharField(max_length=500)
    done = models.BooleanField(default=False)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.text



