from django.conf.urls import url
from api import QuestionAPIView

urlpatterns = [
    url(r'^question/(?P<pk>\d+)$', QuestionAPIView.as_view(), )
]