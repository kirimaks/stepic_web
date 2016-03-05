from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'qa.views.test', 		name='home'),
    url(r'^login/$', 'qa.views.test', 		name='login'),
    url(r'^ask/$', 'qa.views.test', 		name='ask'),
    url(r'^popular/$', 'qa.views.test',		name='popular'),
    url(r'^new/$', 'qa.views.test', 		name='new'),
    url(r'^signup/$', 'qa.views.test', 		name='signup'),
    url(r'^question/(?P<qid>[0-9]+)/$', 'qa.views.test', name='question'),

    url(r'^admin/', include(admin.site.urls)),
)
