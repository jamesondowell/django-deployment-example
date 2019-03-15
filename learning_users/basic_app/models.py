from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    PROF_DESIGNATION = (
        ('SCM', 'Supply Chain Manager'),
        ('3PL', '3PL Service Provider'),
        ('INC', 'Independent Consultant'),
        ('OTH', 'Other'),
    )

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User,on_delete = models.CASCADE)

    # Add any additional attributes you want
    portfolio_site = models.URLField(blank=True)
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    prof_desig = models.CharField(max_length=3,choices=PROF_DESIGNATION,default='SCM')
    opt_news = models.BooleanField(default=False)



    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
