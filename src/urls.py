from django.conf.urls import url, include

urlpatterns = [
    url(r'^_ah/', include('djangae.urls')),
    url(r'^$', 'project.home.views.index'),
    url('^api/docs/', include('rest_framework_docs.urls')),
    url(r'^api/', include('project.api.urls')),
    url(r'^home/', include('project.home.urls')),
    url(r'^polls/', include('project.polls.urls')),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^accounts/', include('registration.auth_urls'))
]
