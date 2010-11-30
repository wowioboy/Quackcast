from django.contrib import admin
from podcast.models import *

class ThumbsInline(admin.StackedInline):
    model = Thumbs
    extra = 3

class PodcastAdmin(admin.ModelAdmin):
    inlines = [ThumbsInline]
    search_fields = ['title']
    list_display = ('title','isactive', 'pub_date')
    list_filter = ('pub_date', 'isactive')
    prepopulated_fields = {"slug" : ('title',)}

admin.site.register(Podcast,PodcastAdmin)
