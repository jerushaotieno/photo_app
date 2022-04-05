from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django_registration.backends.one_step.views import RegistrationView


from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    url('^$',views.user_feed,name = 'user_feed'),
    url(r'^user_profile/$', views.user_profile, name='user_profile'),
    url('^search/', views.search, name='search'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/',
        RegistrationView.as_view(success_url=reverse_lazy('home')),
        name='django_registration_register'),

    path(r'logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path(r'login/', LoginView.as_view(), {"next_page": '/'}),
]

urlpatterns += staticfiles_urlpatterns()


# if settings.DEBUG:
#     urlpatterns+=STATIC_URL(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
