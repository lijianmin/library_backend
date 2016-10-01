from django.db                      import models
from django.contrib.auth.models     import User
from rest_framework                 import permissions

class UserProfile(models.Model):

    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    country = (
        ('SG','Singapore'),
    )

    country = models.CharField(max_length = 4, choices = country, default='SG')

    gender = (
        ('M', 'Female'),
        ('F', 'Male'),
    )

    gender = models.CharField(max_length = 2, choices = gender, default='F')

    # The additional attributes we wish to include.
    zip_code = models.CharField(max_length = 10)
    birthday = models.DateField(null=True)
    home_address = models.TextField()
    mobile_no = models.CharField(max_length = 20)

