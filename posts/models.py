from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)
    body = RichTextField(blank=True, null=True) #ckeditor
    category = models.CharField(max_length=100, choices=[
        ('ai', 'Artificial Intelligence'),
        ('web', 'Web Development'),
        ('coding', 'Coding'),
        ('tech', 'Technology'),
        ('featured', 'Featured'),
        ('foryou', 'For you'),
    ], default='foryou')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.title

# comments:
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
