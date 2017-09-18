from django.conf.urls import url

from views import homepage, tag_detail

urlpatterns = [
    url(r'^tag_detail/(?P<slug>[\w\-]+)/$', tag_detail, name='tag_detail'),
    url(r'^$', homepage),
]
