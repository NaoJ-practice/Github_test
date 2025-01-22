from django.db import models
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    scheduled_date = models.DateTimeField(default=now)
    is_published = models.BooleanField(default=False)

def __str__(self):
    return self.title

