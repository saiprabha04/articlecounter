from django.db import models

# Create your models here.
class ArticleT(models.Model):
    articlename=models.CharField(max_length=50)
    slug=models.SlugField()
    counter=models.IntegerField()

    
    