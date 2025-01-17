from django.urls import path

from . import views
from .views import ProtectedView 

urlpatterns = [
    path('categories/', views.CategoryListCreateAPIView.as_view()),
    path('categories/<int:pk>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('protected-endpoint/', ProtectedView.as_view(), name='protected-view'),

]


