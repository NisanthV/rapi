from django.urls import path,include
#from rest_framework_simplejwt.view import TokenObtainPairView,TokenRefreshView
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView
from . import views
urlpatterns=[
    path('',views.Authenticate.as_view()),
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),
    path('auth/',include('rest_framework.urls')),
    path('create/',views.CreateNotes.as_view()),
    path('delete/<int:pk>',views.DeleteNotes.as_view()),
]