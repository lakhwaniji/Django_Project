from django.db import models


class Form(models.Model):
    first = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    occupation = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()

    def __str__(self):
        return f"{self.first}{self.last_name}"
