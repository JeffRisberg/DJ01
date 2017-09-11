from django.conf.urls import url

from views import greeting

urlpatterns = [
    url(r'^$', greeting),
]