from django.db import models

# Create your models here.
class news(models.Model):
    id_news = models.IntegerField(default=00000000,primary_key=True,unique=True)
    title_news = models.CharField(max_length=50)
    des_news = models.CharField(max_length=1580)
    auteur_news = models.CharField(max_length=50)
    image_news1 = models.ImageField(null=True,blank=True)
    image_news2 = models.ImageField(null=True,blank=True)
    image_news3 = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.title_news
