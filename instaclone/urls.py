from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    url('^$',views.user_feed,name = 'user_feed'),
    url(r'^user_profile/$', views.user_profile, name='user_profile'),
    url('^search/', views.search, name='search'),
]

urlpatterns += staticfiles_urlpatterns()


# if settings.DEBUG:
#     urlpatterns+=STATIC_URL(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
