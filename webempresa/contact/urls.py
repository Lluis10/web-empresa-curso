from django.urls import path
from . import views as core_views

urlpatterns = [
    # Paths Core
    path('', core_views.contact, name='contact'),
]
