from django.db import models
# import datetime
# Create your models here.


# Create your models here.
class Blog(models.Model):
    def __str__(self):
        return self.author
    img = models.ImageField(upload_to="images")
    title=models.CharField(max_length=100)
    desc=models.TextField()
    author=models.CharField(max_length=100)
