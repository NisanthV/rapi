from django.urls import path
from . import views

urlpatterns = [
    path('', views.Createapi.as_view()),
    path('<int:pk>/',views.ProductDetailsAPI.as_view()),
    path('show/',views.ListClass.as_view()),
]
