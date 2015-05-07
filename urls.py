from django.http import HttpResponsePermanentRedirect
from django.conf.urls import *

urlpatterns = patterns('',
    (r'^/soldier/all$', lambda request: HttpResponsePermanentRedirect('/wardead/contribute')),
    (r'^/soldier/(?P<soldiername>[0-9]+)$', 'wardead.views.DetailID'),
    (r'^/soldier/(?P<soldiername>[a-zA-Z_.-]+)/story$', 'wardead.views.Story'),
    (r'^/soldier/(?P<soldiername>[a-zA-Z_.-]+)$', 'wardead.views.Detail'),
    (r'^/state/(?P<state>[a-zA-Z_.-]+)$', 'wardead.views.StatePage'),
    (r'^/search$', 'wardead.views.Search'),
    (r'^', 'wardead.views.Main'),
)

