from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 		'qa.views.home', name='home'),
    url(r'^login/$', 	'qa.views.login', name='login'),
    url(r'^ask/', 	'qa.views.ask',  name='ask'),
    url(r'^popular/$', 	'qa.views.best', name='popular'),
    url(r'^new/$', 	'qa.views.test', name='new'),
    url(r'^signup/$', 	'qa.views.signup', name='signup'),
    url(r'^question/(?P<qid>[0-9]+)/$', 'qa.views.question', name='question'),

    url(r'^admin/', include(admin.site.urls)),
)
