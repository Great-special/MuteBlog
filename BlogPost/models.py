from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from .utils import generate_slug



# Create your models here.


class BlogModel(models.Model):
    CHOICES = (
        ('life-style', 'LIFESTYLE'),
        ('journey', 'JOURNEY'),
        ('inspiration', 'INSPIRATION'),
    )
    author = models.ForeignKey(User, blank=True, null=True,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, null=False, blank=True)
    image = models.ImageField(upload_to='blogPost/')
    category = models.CharField(max_length=125, choices=CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        
        super(BlogModel, self).save(*args, **kwargs)
    
    @property
    def get_image_url(self):
        image_url = self.image.url
        # print("Image URL", image_url)
        return image_url


class BlogComment(models.Model):
    post = models.ForeignKey(BlogModel, blank=True, null=True, on_delete=models.CASCADE, related_name="comment")
    comment = models.TextField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class CommentReply(models.Model):
    comment = models.ForeignKey(BlogComment, on_delete=models.CASCADE)
    reply = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.reply

  
class Profile(User):
    image = models.ImageField(upload_to='profile/')
    info = models.TextField(max_length=200)
    
    