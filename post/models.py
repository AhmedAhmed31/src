from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = RichTextField()
    img = models.ImageField(upload_to='post_img/')
    created = models.DateTimeField(default=timezone.now)
    Publish=models.BooleanField(default=True)


    def __str__(self):
        return self.title
