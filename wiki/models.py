from django.db import models
from filebrowser.fields import FileBrowseField


# Create your models here.
class Article(models.Model):
    title = models.CharField(u"Title", max_length=250, blank=True, null=True)
    image = FileBrowseField("Image", max_length=200, directory="media/", extensions=[".jpg", ".png"], blank=True, null=True)
    url = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "title__icontains",)

class Visitor(models.Model):
    name = models.CharField(max_length=130)
    # gender = models.CharField(max_length=130)
    # hobby1 = models.CharField(max_length=250)
    # hobby2= models.CharField(max_length=250)
    # fav_book = models.CharField(max_length=250)
    # fav_movie = models.CharField(max_length=250)
    email = models.EmailField(blank=True)
    job_title = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name
