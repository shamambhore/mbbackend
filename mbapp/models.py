from distutils.command.upload import upload
from email.policy import default
from operator import mod
from pyexpat import model
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.postgres.fields import ArrayField


turn_around_time_choice =(
    ('6-7 weeks','6-7 weeks'),
)

sample_required_choice = (
    ('st', 'Stool'),
)

sample_collection_choice = (
    ('home','At Home'),
)

fasting_required_choice = (
    ('n','No'),
    ('y', 'yes'),
)
class Productpackage(models.Model):
    package_title = models.CharField(max_length=100)
    package_category = models.CharField(max_length=100)
    package_newprice = models.PositiveIntegerField()
    package_oldprice = models.PositiveIntegerField()
    package_description = models.CharField(max_length=1000)
    Package_points = ArrayField(models.CharField(max_length=1000), blank=True, null=True)    
    home_images = models.ImageField(upload_to="media/", blank=True, null=True)
    inclusion_points = ArrayField(models.CharField(max_length=5000), blank=True, null=True)
    turn_around_time = models.CharField(max_length=100, choices=turn_around_time_choice, blank=True, null=True)
    sample_required = models.CharField(max_length=100,choices=sample_required_choice, blank=True, null=True)
    sample_collection = models.CharField(max_length=100,choices=sample_collection_choice, blank=True, null=True)
    fasting_required = models.CharField(max_length=100,choices=fasting_required_choice, blank=True, null=True)
    addon_name = ArrayField(models.CharField(max_length=100), null=True, blank=True)
    addon_description = ArrayField(models.CharField(max_length=100), null=True, blank=True)
    addon_price = ArrayField(models.PositiveIntegerField(), null=True, blank=True)
    
    
    def __str__(self):
        return self.package_category
    
class Packageimages(models.Model):
    product= models.ForeignKey(Productpackage, on_delete=models.CASCADE)
    product_images = models.ImageField(upload_to="media/", blank=True, null=True)

