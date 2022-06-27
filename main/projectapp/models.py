from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Main(models.Model):
    title = models.CharField(max_length = 200 , default = '제목' )
    people = models.CharField(max_length= 100 )
    pub_date = models.DateTimeField('date' , blank = True)
    body = models.TextField()
    how = models.CharField(max_length = 100 , null=True)

    def __str__(self):
        return self.title
    def __str__(self):
        return self.people
    def __str__(self):
        return self.how    

    