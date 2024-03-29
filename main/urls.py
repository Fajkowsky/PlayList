from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', 'landingpage.views.index', name='index'),
    url(r'^frontpage/$', 'landingpage.views.frontpage', name='frontpage'),
    url(r'^register/$', 'landingpage.views.register', name='register'),
    url(r'^addsong/$', 'landingpage.views.addsong', name='addsong'),
    url(r'^mysong/$', 'landingpage.views.mysong', name='mysong'),
    url(r'^logout/$', 'landingpage.views.logouting', name='logouting'),

    url(r'^admin/', include(admin.site.urls)),
)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )