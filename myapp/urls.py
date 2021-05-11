from django.urls import path
from . import views

urlpatterns = [
    path('realtor/',views.index,name='home'),
]
