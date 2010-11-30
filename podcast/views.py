from django.core.exceptions import ObjectDoesNotExist
from django.utils import encoding
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Context, loader
from django.http import Http404
from podcast.models import *

# Create your views here.

def home_page(request):

  latest_podcasts = Podcast.objects.select_related().order_by('-pub_date').filter(isactive=1)[:5]
  variables = RequestContext(request, {
    'latest_podcasts':latest_podcasts,
  })
  return render_to_response('podcast/index.html', variables)
    
def detail(request, slug):
    try:
        p = Podcast.objects.get(slug=slug)
    except Podcast.DoesNotExist:
        raise Http404
    return render_to_response('podcast/detail.html', {'podcast': p})    
