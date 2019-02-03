# from django.urls import path
# from . import views


# urlpatterns = [
#      path('location/', views.get_post_locations.as_view(), name="location-all")
# ]
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^location/(?P<pk>[0-9]+)$', # urls with details i.e /movies/(1-9)
        views.get_delete_update_location,
        name='get_delete_update_location'
    ),   
    url(
        r'^locations/$', # urls list all and create new one
        views.get_post_locations,
        name='get_post_locations'
    ),   
]