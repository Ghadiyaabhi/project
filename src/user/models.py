from django.db import models
# from hospital.models import Doctor


class forgotpassword(models.Model):
      email = models.EmailField(default=True)

def __str__(self):
    return self.email