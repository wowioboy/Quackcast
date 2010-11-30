import os
from django.conf.urls.defaults import *
#from django.views.generic.simple import direct_to_template
from django.contrib import admin
from podcast.views import *

admin.autodiscover()

media = os.path.join(os.path.dirname(__file__), 'media')

urlpatterns = patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': media, 'show_indexes': True}),
    (r'^tagging_autocomplete/', include('tagging_autocomplete.urls')),
    
    # views
    (r'^$', home_page),
    (r'^podcast/', include('podcast.urls')),
)