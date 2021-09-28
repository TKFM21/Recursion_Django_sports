from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('<int:pk>/', views.Index.as_view(), name='index'),
    path('<int:pk>/rule/', views.RuleIndex.as_view(), name='rule'),
    path('<int:pk>/pickups/', views.PickupsIndex.as_view(), name='pickups'),
    path('<int:pk>/pickups/<int:id>/', views.PickupDetail.as_view(), name='pickup'),
    path('<int:pk>/links/', views.Links.as_view(), name='links'),
]
