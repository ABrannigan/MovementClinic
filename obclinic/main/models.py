from django.db import models
from datetime import datetime
# Create your models here.
class BlogPost(models.Model):
    post_title = models.CharField(max_length=200)
    post_content = models.TextField()
    post_date = models.DateTimeField('published on', default=datetime.now())

    def __str__ (self):
        return self.post_title
