from . import views
from django.urls import path

urlpatterns=[
  path('', views.hello),
  path('testing/', views.testing)
]