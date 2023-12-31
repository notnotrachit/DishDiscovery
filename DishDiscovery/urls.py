"""
URL configuration for DishDiscovery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .views import index
from django.conf import settings
from django.conf.urls.static import static
from recipe import views as recipe_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('accounts/', include('allauth.urls')),
    path('recipes/', recipe_views.all_recipes, name='all_recipes'),
    path('recipes/<int:pk>/', recipe_views.recipe_detail, name='recipe_detail'),
    path('recipes/new/', recipe_views.new_recipe, name='new_recipe'),
    path('recipes/<int:pk>/like/', recipe_views.toggle_like_recipe, name='toggle_like_recipe'),
    path('recipes/<int:pk>/edit/', recipe_views.edit_recipe, name='edit_recipe'),
    path('accounts/profile/', recipe_views.profile, name='profile'),
    path('recipes/search/', recipe_views.search, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)