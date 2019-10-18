from django.db import models

# Create the Blog models here.
class Blog(models.Model):
    titel = models.CharField(max_length=225)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='image/')
