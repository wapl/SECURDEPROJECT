from django.urls import path 
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('search/', views.SearchView, name='search_results'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='detail'),
    path('reviews/new//<int:pk>/', views.ReviewCreateView.as_view(), name='review-create'),
    path('reserve/<pk>', views.ReserveBook, name='reserve'),
]