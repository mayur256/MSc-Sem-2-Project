from django.conf.urls import url
from blog import views
from django.conf import settings
from django.conf.urls.static import static
app_name="blog"
urlpatterns = [
    url(r'(?P<id>\d+)/post_edit/$', views.post_edit, name="post_edit"),
    url(r'(?P<reqid>\d+)/(?P<proid>\d+)/(?P<posid>\d+)/(?P<comid>\d+)/report/$', views.report, name="report"),
    url(r'(?P<id>\d+)/post_delete/$', views.post_delete, name="post_delete"),
    url(r'(?P<id>\d+)/cmnt_delete/$', views.cmnt_delete, name="cmnt_delete"),
    url(r'(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.post_detail, name="post_detail"),
    url(r'post_create/$', views.post_create, name="post_create"),
    url(r'edit_profile/$', views.edit_profile, name="edit_profile"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)