from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^students/$', views.student_list),
    url(r'^students/(?P<pk>[0-9]+)/$', views.student_detail),
]
