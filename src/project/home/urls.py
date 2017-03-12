from django.conf.urls import url
from views import Home, SuccessLoginView

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^success_login/$', SuccessLoginView.as_view(), name='success_login')
]