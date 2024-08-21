from django.db import models

# Create your models here.
class forgotpassword(models.Model):
    email = models.EmailField(default=True)
    def __str__(self):
        return self.email