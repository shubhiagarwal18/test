"""testproject URL Configuration

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
from django.urls import path, include
from django.conf.urls.static import static
import app1
import app2
from app1.views import *
from app2.views import *
#from testproject import settings
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app1.views.index, name='index'),
    path('save', app1.views.inputs, name='save'),
    path('showdata', app2.views.show_data, name='showdata'), 
    path('view', app2.views.view, name='view'),   
    path('delete', app2.views.delete, name='delete'),   
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
