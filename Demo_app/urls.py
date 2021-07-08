"""Demo_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from user import views
from user.views import Postview,fullpost,addpost
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')), # all url's from user app
    path('products/', include('products.urls')), # all url's from product app
    path('',views.user_login),
    path('fullpost/<int:pk>',fullpost.as_view(),name='fullpost'),
    path('post_page/',Postview.as_view(),name='posts'),
    path('addpost/', addpost.as_view(), name='addpost'),

    # path('post_page/',views.post_page),
    path('logout/', views.user_logout,name='logout')

]
