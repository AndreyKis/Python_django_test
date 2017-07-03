from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.TextField()
    author = models.TextField()
    amount_of_pages = models.IntegerField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title
