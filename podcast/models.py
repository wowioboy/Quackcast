import datetime
from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from tagging.fields import TagField
from tagging.models import Tag
from tagging_autocomplete.models import TagAutocompleteField
from podcast.fields import ThumbnailImageField

class LiveManager(models.Manager):
    def get_query_set(self):
        return super(LiveManager, self).get_query_set().filter(isactive=True).order_by('-pub_date')

class Podcast(models.Model):
    isactive = models.BooleanField('Is Active On Site?',default=False)
    title = models.CharField("Show Title",max_length=200)
    path = models.CharField(max_length=200,blank=True,null=True)
    leadin = models.TextField("Lead-in Copy",blank=True,null=True)
    detail = models.TextField("Detail Copy",blank=True,null=True)
    pub_date = models.DateTimeField('Published Date',blank=True,null=True)
    url = models.URLField("CDN URL (Internal Use)", max_length=200,blank=True,null=True)
    url_itunes = models.URLField("iTunes URL",max_length=200,blank=True,null=True)
    show_file = models.FileField(upload_to="audio",blank=True,null=True)
    tags = TagAutocompleteField('Tags',help_text='Keywords to help searching for content.')
    slug = models.SlugField(
        unique_for_date='pub_date',
        help_text='Automatically built from the title. -- DO NOT MODIFY',
        blank=True,
        null=True
    )

    objects = models.Manager()  # Declare this manager first to use default manager for admin
    live = LiveManager()

    class Meta:
        ordering = ['title']
        verbose_name = "Shows"
        verbose_name_plural = "Shows"

    def __unicode__(self):
        return self.title

    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()

    def get_tags(self):
        return Tag.objects.get_for_object(self)

    @permalink
    def get_absolute_url(self):
        return "/%s/%s/" %(self.pub_date.strftime("%Y/%b/%d").lower(), self.slug)

class Likes(models.Model):
    podcast = models.ForeignKey(Podcast)
    count = models.IntegerField()
    
    def __unicode__(self):
        return self.count
        
class Thumbs(models.Model):
    podcast = models.ForeignKey(Podcast)
    image = ThumbnailImageField("Thumbnail",upload_to='thumbs')
    class Meta:
        verbose_name = "Thumbnail"
        verbose_name_plural = "Thumbnail Images"

            
