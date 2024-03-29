from django.conf import settings
from django.conf.urls.defaults import patterns, include
from django.contrib import admin as django_admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import direct_to_template, redirect_to

django_admin.autodiscover()

import admin

urlpatterns = patterns('',
    (r'^robots\.txt$', direct_to_template, {'template':'robots.txt', 'mimetype':'text/plain'}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^student/competion/fall/$', redirect_to, {'url':'/student/competition/fall/'}),
    (r'^admin/', include(django_admin.site.urls)),
    (r'^ckeditor/', include('ckeditor.urls')),
)

urlpatterns += patterns('core.views',
   (r'^$', 'home', {}, 'home'),
   (r'^about/$', 'about', {}, 'about'),
   (r'^photos/$', 'photos', {}, 'photos'),
   (r'^applicant-poll/$', 'applicant_poll', {}, 'applicant_poll')
)

urlpatterns += patterns('event.views',
    (r'^events/$', 'events_upcoming', {}, 'events_upcoming'),
    (r'^events/past/$', 'events_past', {}, 'events_past')   
)

urlpatterns += staticfiles_urlpatterns()
