"""
main url configuration file for the askbot site
"""
from django.conf.urls.defaults import patterns, include, handler404, handler500, url
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from modelresourceexample.resources import MyModelResource

from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'%s' % settings.ASKBOT_URL, include('askbot.urls')),
    (r'^admin/', include(admin.site.urls)),
    #(r'^cache/', include('keyedcache.urls')), - broken views disable for now
    (r'^settings/', include('askbot.deps.livesettings.urls')),
    (r'^followit/', include('followit.urls')),
    (r'^robots.txt$', include('robots.urls')),
    url(r'^$', ListOrCreateModelView.as_view(resource=MyModelResource), name='mobile_resource'),
    url(r'^(?P<pk>[0-9]+)/$', InstanceModelView.as_view(resource=MyModelResource)),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
                    url(r'^rosetta/', include('rosetta.urls')),
                )
