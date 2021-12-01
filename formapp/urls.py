from django.urls import path
from  . import views
urlpatterns=[
    path('',views.fnabc, name='user')
    
]