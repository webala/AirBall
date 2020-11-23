from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    publisher = models.CharField(max_length=50)
    date_published = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']