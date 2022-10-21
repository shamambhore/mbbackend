from distutils.command.upload import upload
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Package(models.Model):
    package_title = models.CharField(max_length=100)
    package_category = models.CharField(max_length=100)
    package_newprice = models.PositiveIntegerField()
    package_oldprice = models.PositiveIntegerField()
    package_description = models.CharField(max_length=1000)
 
    def __str__(self):
        return self.package_category

class Homeimages(models.Model):
    home_images = models.ImageField(upload_to="media")

    def __str__(self):
        return str(self.home_images)

class Packageimages(models.Model):
    package_images = models.ImageField(upload_to="media")

    def __str__(self):
        return str(self.package_images)