"""SuixinSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from myblog.views import IndexView, BlogDetailView, AddCommentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', IndexView.as_view(), name='index'),
    path('blog/(?P<blog_id>\d+)$', BlogDetailView.as_view(), name='detail'),
    path('add_comment/', AddCommentView.as_view(), name='add_comment'),
]
