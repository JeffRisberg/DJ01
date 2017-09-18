from django.conf.urls import url

from views import homepage, tag_detail

urlpatterns = [
    url(r'^tag/(?P<slug>[\w\-]+)/$',
        tag_detail,
        ),
    url(r'^$', homepage),
]
