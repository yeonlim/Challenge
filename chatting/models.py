from django.db import models
from django.contrib.auth.models import User
    
# Create your models here.
class Message(models.Model):
    to = models.CharField(max_length=50)
    writer = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE, null=False)
    pub_date = models.DateTimeField()
    body = models.TextField("쪽지")
    
    def summary(self):
        return self.body[:20]