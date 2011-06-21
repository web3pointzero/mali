from django.db import models

class Haber(models.Model):
    title = models.CharField(max_length=115)
    content = models.TextField (blank=True)
    publication_date = models.DateField(blank=True)

    def __unicode__(self):
        return self.title

class Makale(models.Model):
    title = models.CharField(max_length=115)
    content = models.TextField (blank=True)
    author = models.CharField(max_length=115)
    #image = models.ImageField???
    publication_date = models.DateField(blank=True)

    def __unicode__(self):
        return self.title

class Notdefteri(models.Model):
    title = models.CharField(max_length=115)
    content = models.TextField (blank=True)
    author = models.CharField(max_length=115)
    #image = models.ImageField???
    publication_date = models.DateField(blank=True)

    def __unicode__(self):
        return self.title

