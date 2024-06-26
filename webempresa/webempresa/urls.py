"""
URL configuration for webempresa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from core import views as core_views
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    # Paths Admin
    path('admin/', admin.site.urls),

    # Paths Core
    path('', include('core.urls')),

    # Paths Services
    path('services/', include('Services.urls')),

    # Paths Blog
    path('blog/', include('blog.urls')),

    # Paths Pages
    path('page/', include('pages.urls')),

    # Paths Pages
    path('contact/', include('contact.urls')),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
