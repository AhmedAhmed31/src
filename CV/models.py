from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class CV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    Edcaction = RichTextField()
    profile = models.ImageField(upload_to='post_img/',default="post_img/default.png",null=True)
    created = models.DateTimeField(default=timezone.now)
    Publish=models.BooleanField(default=True)

    def __str__(self):
        return self.Name
