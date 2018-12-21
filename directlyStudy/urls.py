from django.contrib import admin
"""directlyStudy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from FoodSearch import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.init),
    url(r'^admin/', admin.site.urls),
    url(r'^showJson/', views.show_json),
    url(r'^detailInformation(\d+)/$', views.detail_information),
    url(r'^showdetail(\d+)/$', views.show_detail),
    url(r'^inputVoice/', views.input_voice)
]


