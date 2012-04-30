from django.conf import settings
from django.conf.urls.defaults import patterns, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
    (r'^robots\.txt$', direct_to_template, {'template':'robots.txt', 'mimetype':'text/plain'}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^ckeditor/', include('ckeditor.urls')),
)

urlpatterns += patterns('core.views',
   (r'^$', 'home', {}, 'home'),
   (r'^about$', 'about_us', {}, 'about_us')
)

urlpatterns += patterns('event.views',
    (r'^events/$', 'events', {}, 'events'),   
)

urlpatterns += staticfiles_urlpatterns()
