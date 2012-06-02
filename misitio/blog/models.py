from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __unicode__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateTimeField()
    authors = models.ManyToManyField(Author)

    def __unicode__(self):
        return self.title


