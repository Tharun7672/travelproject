from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('',views.contact, name='contact'),
    path('',views.destinations, name='destinations')
]
