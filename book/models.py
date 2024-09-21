from django.db import models

# Create your models here.


class Book(models.Model):

    title = models.CharField(max_length=50, unique=True)
    author_name = models.CharField(max_length=15)
    author_surname = models.CharField(max_length=20)
    page_num = models.IntegerField()
    description = models.CharField(max_length=250)


    def __str__(self):
        return f' The title of the book is {self.title}, name of the author {self.author_name} {self.author_surname}, description of the book: {self.description}, number of pages: {self.page_num}!!! \n '
