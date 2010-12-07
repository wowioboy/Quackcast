from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from podcast.models import *

# Create your views here.

def home_page(request):

    search = False
    date = False
    podcasts = Podcast.live.all()
    
    if 'search' in request.GET:
        search = request.GET['search'].strip()
        if search != 'search quackcasts':
            podcasts = podcasts.filter(title__icontains=search) | podcasts.filter(detail__icontains=search) | podcasts.filter(leadin__icontains=search)
    
    if 'date' in request.GET:
        date = request.GET['date']
        podcasts = podcasts.filter(pub_date__icontains=date)
        
    variables = RequestContext(request, {
        'podcasts':podcasts,
        'search': search,
        'date': date
    })
    
    #return render_to_response('podcast/index.html', variables)
    return render_to_response('podcast/index_oldmod.html', variables)
    
def detail(request, slug):
    
    p = get_object_or_404(Podcast, slug=slug)
    return render_to_response('podcast/detail.html', {'podcast': p})    
