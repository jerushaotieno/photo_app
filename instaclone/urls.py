from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^user_profile/$', views.user_profile, name='user_profile'),
]

urlpatterns += staticfiles_urlpatterns()