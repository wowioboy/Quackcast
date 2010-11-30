import os
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from tagging.views import tagged_object_list
from django.conf import settings
from podcast.models import *
from podcast.views import *

entries = Podcast.objects.select_related().order_by('-pub_date','title').filter(isactive=1)[:5]
data_dict = {
	'queryset': entries,
	'date_field': 'pub_date',
}

urlpatterns = patterns('django.views.generic.date_based',
    (r'(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', 'object_detail', dict(data_dict, template_name='podcast/detail.html')),
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', 'object_detail', dict(data_dict, template_name='podcast/detail.html')),
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$','archive_day',dict(data_dict,template_name='podcast/index.html')),
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$','archive_month', dict(data_dict, template_name='podcast/index.html')),
    (r'^(?P<year>\d{4})/$','archive_year', dict(data_dict, template_name='podcast/index.html')),
    (r'^$',home_page),
)
