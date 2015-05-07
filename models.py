from django.db import models
from django.template.defaultfilters import slugify
from django.utils.encoding import *
from django.utils.http import *

class WarDead(models.Model):
    service = models.CharField(max_length=30)
    component = models.CharField(max_length=30, help_text="National Guard, Reserve, etc.)", null=True, blank=True)
    name = models.CharField(max_length=50, help_text="Last, Fire Middle")
    last = models.CharField(max_length=50, null=True, blank=True)
    rest = models.CharField(max_length=50, null=True, blank=True)
    quote = models.TextField(help_text="A great quote about the soldier", blank=True, null=True)
    quotesource = models.CharField(max_length=100, null=True, blank=True)
    mugshot = models.ImageField(upload_to='wardeadmugs/', max_length=100, null=True, blank=True)
    other_photo = models.ImageField(upload_to='warotherphotos/', max_length=100, null=True, blank=True)
    other_photo_cutline = models.TextField(null=True, blank=True)
    rank = models.CharField(max_length=25, null=True, blank=True)
    pay = models.CharField(max_length=3, null=True, blank=True)
    date = models.DateField()
    hostile = models.CharField(max_length=1, help_text="'H' if killed by hostile, blank if not", null=True, blank=True)
    notwardeadflag = models.BooleanField()
    cause_of_death = models.CharField(max_length=100, null=True, blank=True)
    age= models.IntegerField()
    gender = models.CharField(max_length=1, help_text = "M or F")
    homecity = models.CharField(max_length=50, blank=True, null=True)
    homecounty = models.CharField(max_length=20, null=True, blank=True)
    homestate = models.CharField(max_length=50)
    unit = models.CharField(max_length=75, blank=True, null=True)
    deathcountry = models.CharField(max_length=50, blank=True, null=True)
    deathcity = models.CharField(max_length=50, blank=True, null=True)
    race = models.CharField(max_length=30, blank=True, null=True)
    war = models.CharField(max_length=60, help_text="Iraq, Afghanistan, other alert Matt", blank=True, null=True)
    story = models.TextField(null=True, blank=True)
    nameslug = models.CharField(max_length=50, editable=False, null=True, blank=True)
    enable_comments = models.BooleanField(default='1')
    def __unicode__(self):
        return self.nameslug
    def save(self):
        if not self.mugshot:
            self.mugshot = "wardeadmugs/%s.jpg" % slugify(self.name)
        self.nameslug = slugify(self.name)
        super(WarDead, self).save()
    def get_absolute_url(self):
        return "/wardead/soldier/$s" % self.nameslug    