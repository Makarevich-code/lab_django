from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('how-to-find/', views.how_to_find, name='how_to_find'),
    path('poster/', views.poster, name='poster'),
    path('troupe/', views.troupe, name='troupe'),

    # Workers
    path('workers/', views.WorkerListView.as_view(), name='worker_list'),
    path('workers/<int:pk>/', views.WorkerDetailView.as_view(), name='worker_detail'),
    path('workers/create/', views.WorkerCreateView.as_view(), name='worker_create'),
    path('workers/<int:pk>/edit/', views.WorkerUpdateView.as_view(), name='worker_update'),
    path('workers/<int:pk>/delete/', views.WorkerDeleteView.as_view(), name='worker_delete'),

    # Performances
    path('performances/', views.PerformanceListView.as_view(), name='performance_list'),
    path('performances/<int:pk>/', views.PerformanceDetailView.as_view(), name='performance_detail'),
    path('performances/create/', views.PerformanceCreateView.as_view(), name='performance_create'),
    path('performances/<int:pk>/edit/', views.PerformanceUpdateView.as_view(), name='performance_update'),
    path('performances/<int:pk>/delete/', views.PerformanceDeleteView.as_view(), name='performance_delete'),

    # Genres
    path('genres/', views.GenreListView.as_view(), name='genre_list'),
    path('genres/<int:pk>/', views.GenreDetailView.as_view(), name='genre_detail'),
    path('genres/create/', views.GenreCreateView.as_view(), name='genre_create'),
    path('genres/<int:pk>/edit/', views.GenreUpdateView.as_view(), name='genre_update'),
    path('genres/<int:pk>/delete/', views.GenreDeleteView.as_view(), name='genre_delete'),

    # Roles
    path('roles/', views.RoleListView.as_view(), name='role_list'),
    path('roles/<int:pk>/', views.RoleDetailView.as_view(), name='role_detail'),
    path('roles/create/', views.RoleCreateView.as_view(), name='role_create'),
    path('roles/<int:pk>/edit/', views.RoleUpdateView.as_view(), name='role_update'),
    path('roles/<int:pk>/delete/', views.RoleDeleteView.as_view(), name='role_delete'),

    # Awards
    path('awards/', views.AwardListView.as_view(), name='award_list'),
    path('awards/<int:pk>/', views.AwardDetailView.as_view(), name='award_detail'),
    path('awards/create/', views.AwardCreateView.as_view(), name='award_create'),
    path('awards/<int:pk>/edit/', views.AwardUpdateView.as_view(), name='award_update'),
    path('awards/<int:pk>/delete/', views.AwardDeleteView.as_view(), name='award_delete'),
]
