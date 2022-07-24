from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('data published')
    writer = models.CharField(max_length = 20 , null = True , blank = True )
    feeling = models.CharField(max_length= 100)
    body=models.TextField()
    image = models.ImageField(upload_to = 'images/' , blank = True , null = True)
    

    def __str__(self):
        return self.title

class Comment(models.Model) : 
    def __str__(self):
        return self.text

    blog_id = models.ForeignKey(Blog, on_delete = models.CASCADE, related_name = 'comments' )  
    text= models.CharField(max_length = 50) 