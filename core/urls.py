from django.urls import path
from . import views
from .views import ABC, SignUp, spider, graph

urlpatterns = [

    path('',ABC.as_view(),name='abc'),
    path('spider', spider,name='spider'),
    path('graph', graph,name='graph'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]