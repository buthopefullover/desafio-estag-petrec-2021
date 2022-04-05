from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=120)
    details = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

