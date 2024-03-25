from django.urls import path
from . import views as core_views

urlpatterns = [
    # Paths Core
    path('', core_views.home, name='home'),
    path('about-me', core_views.about, name='about'),
    path('store', core_views.store, name='store'),
]
