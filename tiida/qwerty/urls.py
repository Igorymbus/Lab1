from django.urls import path
from . import views

urlpatterns = [
    path('', views.info, name='info'),
    
    path('albums/', views.AlbumListView.as_view(), name='album-list'),
    path('albums/<int:pk>/', views.AlbumDetailView.as_view(), name='album-detail'),
    path('albums/create/', views.AlbumCreateView.as_view(), name='album-create'),
    path('albums/<int:pk>/update/', views.AlbumUpdateView.as_view(), name='album-update'),
    path('albums/<int:pk>/delete/', views.AlbumDeleteView.as_view(), name='album-delete'),
    
    path('artists/', views.ArtistListView.as_view(), name='artist-list'),
    path('artists/<int:pk>/', views.ArtistDetailView.as_view(), name='artist-detail'),
    path('artists/create/', views.ArtistCreateView.as_view(), name='artist-create'),
    path('artists/<int:pk>/update/', views.ArtistUpdateView.as_view(), name='artist-update'),
    path('artists/<int:pk>/delete/', views.ArtistDeleteView.as_view(), name='artist-delete'),
    
    path('genres/', views.GenreListView.as_view(), name='genre-list'),
    path('genres/<int:pk>/', views.GenreDetailView.as_view(), name='genre-detail'),
    path('genres/create/', views.GenreCreateView.as_view(), name='genre-create'),
    path('genres/<int:pk>/update/', views.GenreUpdateView.as_view(), name='genre-update'),
    path('genres/<int:pk>/delete/', views.GenreDeleteView.as_view(), name='genre-delete'),
]
