from django.conf.urls import url

from views import index, detail, results, vote

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', vote, name='vote')
]