from django.db                      import models
from django.contrib.auth.models     import User
from rest_framework                 import permissions

class UserProfile(models.Model):

    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    country = (
        ('SG','Singapore'),
        ('MY','Malaysia'),
        ('ID','Indonesia'),
        ('HK','Hong Kong SAR, China'),
    )

    country = models.CharField(max_length = 4, choices = country, default='SG')

    gender = (
        ('M', 'Female'),
        ('F', 'Male'),
        ('UN', 'Unknown'),
    )

    gender = models.CharField(max_length = 2, choices = gender, default='F')

    # The additional attributes we wish to include.

    zip_code = models.CharField(
    	max_length = 6
    )

    birthday = models.DateTimeField(null=True)
    home_address = models.TextField()
    avatar = models.ImageField("Profile Pic", upload_to='avatars/', blank=True, null=True)
    mobile_no = models.CharField(max_length = 20)

