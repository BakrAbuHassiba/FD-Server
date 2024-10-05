
from django.db import models


class Service(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    bgImg = models.ImageField(upload_to='bg_images/')
    txt = models.CharField(max_length=100)
    subTitle = models.TextField(max_length=500, null=True)
    paragraph = models.TextField(max_length=3500, null=True)
    points = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.txt


class Project(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    projectImg = models.ImageField(upload_to='project_images/')
    projectTitle = models.CharField(max_length=500)
    date = models.CharField(max_length=100)
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.projectTitle


class News(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    image = models.ImageField(upload_to='news_images/')
    title = models.CharField(max_length=500)
    date = models.CharField(max_length=100)
    paragraph = models.CharField(max_length=3500)
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Trianing(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=500)
    pointsData = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.title
