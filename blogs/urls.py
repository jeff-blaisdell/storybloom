from django.conf.urls import patterns, url
from blogs import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<category_id>\d)/(?P<post_id>\d)/$', views.get_post, name='post'),
    url(r'^(?P<category_id>\d)/$', views.get_category, name='post')
)