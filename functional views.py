from myproject.wardead.models import *
from django.shortcuts import *
from django.db.models import *
from django.contrib.comments import Comment
from django.core.urlresolvers import reverse

def Main(request):
    commentlist = Comment.objects.filter(content_type="11", is_public="1").order_by('-submit_date')[:10]
    soldiers = WarDead.objects.exclude(name="all").order_by('-date')
    totalcount = soldiers.aggregate(Count('pk'))

    dictionaries = { 'soldiers': soldiers, 'totalcount': totalcount, 'commentlist': commentlist, }
    return render_to_response('wardead/main.html', dictionaries)

def DetailID(request, soldiername):
    soldier = slugify(WarDead.objects.get(pk=soldiername).name)
    place = '/wardead/soldier/' + soldier
    return redirect(place)

def Search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(name__icontains=query)
        )
        results = WarDead.objects.filter(qset).order_by('name')
    else:
        results = []
    return render_to_response("wardead/search.html", {
        "results": results,
        "query": query,
    })

def Contribute(request):
    soldier = WarDead.objects.get(nameslug='all')
    commentlist = Comment.objects.filter(content_type="11", is_public="1").order_by('-submit_date')
    dictionaries = { 'commentlist': commentlist, 'soldier': soldier, }
    return render_to_response('wardead/contribute.html', dictionaries)

def AfghanContribute(request):
    soldier = AfghanContribution.objects.get(pk="2")

    commentlist = Comment.objects.filter(Q(content_type="54") | Q(content_type="15"), Q(is_public="1")).order_by('-submit_date')
    dictionaries = { 'commentlist': commentlist, 'soldier': soldier, }
    return render_to_response('wardead/afghan-contribute.html', dictionaries)	
	
def Detail(request, soldiername):
    soldier = WarDead.objects.get(nameslug=soldiername)
    if soldier.pk != 1:
        previous = WarDead.objects.get(pk=soldier.pk-1)
    else:
        previous = []
    if soldier.pk != 96:
        next = WarDead.objects.get(pk=soldier.pk+1)
    else:
        next = []
    dictionaries = { 'soldier': soldier, 'previous': previous, 'next': next, }
    return render_to_response('wardead/detail.html', dictionaries)

def Story(request, soldiername):
    soldier = WarDead.objects.get(nameslug=soldiername)
    if soldier.pk != 1:
        previous = WarDead.objects.get(pk=soldier.pk-1)
    else:
        previous = []
    if soldier.pk != 96:
        next = WarDead.objects.get(pk=soldier.pk+1)
    else:
        next = []

    dictionaries = { 'soldier': soldier, 'previous': previous, 'next': next, }
    return render_to_response('wardead/story.html', dictionaries)

def comment_posted( request ):
    if request.GET['c']:
        comment_id, post_id  = request.GET['c'].split( ':' )
        post = WarDead.objects.get( pk=post_id )

        if post:
            return HttpResponseRedirect( post.get_absolute_url() )

    return HttpResponseRedirect( "/" )

