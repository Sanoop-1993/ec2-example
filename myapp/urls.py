from django.urls import path
from . import views

urlpatterns = [
   path('articles',views.index,name='index')
]