from django.conf.urls import url, include
from .views import logout, login, register, profile
from . import urls_reset

urlpatterns = [
    url(r'^logout', logout,  name='logout'),
    url(r'^login', login,  name='login'),
    url(r'^register', register,  name='register'),
    url(r'^profile', profile, name='profile'),
    url(r'^password-reset/', include(urls_reset)),
]