from django.urls import path,re_path
from . import views


urlpatterns =[
    path('',views.index,name='index'),
    path('send_email',views.send_email,name='send_email'),
    re_path('search',views.search,name='search')
    
]