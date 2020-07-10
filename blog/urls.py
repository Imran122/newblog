from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('search/', views.search, name='search'),
    path('categorey/', views.categorey, name='categorey'),
    path('post/<id>/', views.post, name='post'),
    
    
]
