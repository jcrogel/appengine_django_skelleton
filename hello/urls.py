from django.conf.urls import patterns, include, url

import hello.views
#import backend.hello as hello


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'hello.views.index', name='index'),
    # url(r'^backend/', include('backend.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
)
