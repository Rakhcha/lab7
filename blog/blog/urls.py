from django.contrib import admin
from django.urls import path
from django.urls import re_path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.archive,name='site'),
    re_path(r'^article/(?P<article_id>\d+)/$',views.get_article,name='get_article'),
    path('article/new/',views.create_post),
    path('newuser/', views.create_user),
    path('login/',views.authorization),
]





