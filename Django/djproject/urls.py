"""djproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import djapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , djapp.views.index, name = 'index'),
    path('create/', djapp.views.create, name = 'create'),
    path('read/', djapp.views.read, name = 'read'),
    path('detail/<str:id>/', djapp.views.detail, name = 'detail'),
    path('edit/<str:id>/', djapp.views.edit, name = 'edit'),
    path('delete/<str:id>/', djapp.views.delete, name = 'delete'),
    path('hashtag/' , djapp.views.hashtag, name = 'hashtag'),
 ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
  

