from django.db import models

# Create your models here.
class Post(models.Model):    
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    people = models.CharField(max_length= 200)
    image = models.ImageField(upload_to= 'images/' ,blank = True )
    def __str__(self):
        return self.title