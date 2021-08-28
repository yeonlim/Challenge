from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Community(models.Model):
    title = models.CharField(max_length=50) #제목
    content = models.TextField() #내용
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="community/", blank = True, null = True)
    image_thumbnail = ImageSpecField(source = 'img', processors=[ResizeToFill(200,200)])

    def __str__(self):
          return self.title

    def summary(self):
        return self.content[:50]

class Comment(models.Model):
    community_id = models.ForeignKey("Community", on_delete=models.CASCADE, db_column="community_id")
    comment_id = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()

class Message(models.Model):
    to_user = models.CharField(max_length=50) #보내는 사람
    from_user = models.CharField(max_length=50) #받는 사람
    message = models.CharField(max_length=500) #메세지 내용

