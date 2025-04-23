from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    about = RichTextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"