from django.db import models

# Create your models here.
class book(models.Model):
    book_name=models.CharField(max_length=(100))
    book_tittle=models.CharField(max_length=(100))
    book_author=models.CharField(max_length=(50))
    book_summary=models.CharField(max_length=(80),null=True)
    pic=models.ImageField(upload_to='images/',null=True)


    def __str__(self):
        return(self.book_name)

