from wardead.models import *
from django.shortcuts import *
from django.db.models import *
from django.core.urlresolvers import reverse

def Main(request):
    soldiers = WarDead.objects.exclude(name="all").exclude(name="Afghan Contributions").exclude(homestate="Missouri").exclude(notwardeadflag="1").order_by('-date')[:9]
    totalcount = soldiers.aggregate(Count('pk'))
    dictionaries = { 'soldiers': soldiers, 'totalcount': totalcount,}
    return render_to_response('wardead/main.html', dictionaries) 

def StatePage(request, state):
    soldiers = WarDead.objects.exclude(name="all").exclude(name="Afghan Contributions").exclude(notwardeadflag="1").filter(homestate=state).order_by('-date')
    state = state
    totalcount = soldiers.count()
    dictionaries = { 'soldiers': soldiers, 'totalcount': totalcount, 'state': state, }
    return render_to_response('wardead/state.html', dictionaries)


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

def Detail(request, soldiername):
    soldiers = WarDead.objects.exclude(name="all").exclude(name="Afghan Contributions").exclude(notwardeadflag="1").order_by('-date')
    soldier = WarDead.objects.get(nameslug=soldiername)
#    if soldier.pk != 1:
#        previous = WarDead.objects.get(pk=soldier.pk-1)
#    else:
#        previous = []
#    if soldier.pk == 90:
#        next = WarDead.objects.get(pk=93)
#    elif soldier.pk != 278:
#        next = WarDead.objects.get(pk=soldier.pk+1)
#    else:
#        next = []
    dictionaries = { 'soldier': soldier, }
    return render_to_response('wardead/detail.html', dictionaries)

def Story(request, soldiername):
    soldiers = WarDead.objects.exclude(name="all").exclude(name="Afghan Contributions").exclude(notwardeadflag="1").order_by('-date')
    soldier = WarDead.objects.get(nameslug=soldiername)
#    if soldier.pk != 1:
#        previous = WarDead.objects.get(pk=soldier.pk-1)
#    else:
#        previous = []
#    if soldier.pk != 278:
#        next = WarDead.objects.get(pk=soldier.pk+1)
#    else:
#        next = []

    dictionaries = { 'soldier': soldier, }
    return render_to_response('wardead/story.html', dictionaries)
