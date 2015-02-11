from django.conf.urls import patterns, url

import increasing.views

urlpatterns = patterns('',

    url(r'^increasingpages/?$', increasing.views.increasing_pages, name='increasing_pages'),
                     
)