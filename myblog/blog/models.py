from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'blog'

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateField()  # Додайте поле publication_date
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    tags = models.ManyToManyField('Tag', related_name='posts')  
    image = models.ImageField(upload_to='post_images/')  

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



# Create your models here.
