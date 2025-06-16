from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Album, Artist, Genre, Track, Label, AlbumArtist

def info(request):
    albums = Album.objects.all().order_by('-id')[:6]  # Получаем 6 последних альбомов
    return render(request, 'qwerty/info.html', {'albums': albums})

class AlbumListView(ListView):
    model = Album
    template_name = 'qwerty/album_list.html'
    context_object_name = 'albums'
    ordering = ['-release_date']

    def get_queryset(self):
        queryset = super().get_queryset()
        genre = self.request.GET.get('genre')
        artist = self.request.GET.get('artist')
        search = self.request.GET.get('search')

        if genre:
            queryset = queryset.filter(genre__name=genre)
        if artist:
            queryset = queryset.filter(artists__name=artist)
        if search:
            queryset = queryset.filter(title__icontains=search)

        return queryset.select_related('genre', 'label').prefetch_related('artists')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        context['artists'] = Artist.objects.all()
        return context

class AlbumDetailView(DetailView):
    model = Album
    template_name = 'qwerty/album_detail.html'
    context_object_name = 'album'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tracks'] = self.object.track_set.all()
        return context

class AlbumCreateView(SuccessMessageMixin, CreateView):
    model = Album
    template_name = 'qwerty/album_form.html'
    fields = ['title', 'release_date', 'price', 'label', 'genre', 'artists', 'cover_image']
    success_url = reverse_lazy('album-list')
    success_message = "Альбом '%(title)s' был успешно создан"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message % form.instance.__dict__)
        return response

class AlbumUpdateView(SuccessMessageMixin, UpdateView):
    model = Album
    template_name = 'qwerty/album_form.html'
    fields = ['title', 'release_date', 'price', 'label', 'genre', 'artists', 'cover_image']
    success_url = reverse_lazy('album-list')
    success_message = "Альбом '%(title)s' был успешно обновлен"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message % form.instance.__dict__)
        return response

class AlbumDeleteView(SuccessMessageMixin, DeleteView):
    model = Album
    template_name = 'qwerty/album_confirm_delete.html'
    success_url = reverse_lazy('album-list')
    success_message = "Альбом был успешно удален"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

# Аналогичные представления для исполнителей
class ArtistListView(ListView):
    model = Artist
    template_name = 'qwerty/artist_list.html'
    context_object_name = 'artists'
    ordering = ['name']

class ArtistDetailView(DetailView):
    model = Artist
    template_name = 'qwerty/artist_detail.html'
    context_object_name = 'artist'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = self.object.album_set.all()
        return context

class ArtistCreateView(SuccessMessageMixin, CreateView):
    model = Artist
    template_name = 'qwerty/artist_form.html'
    fields = ['name', 'country', 'image']
    success_url = reverse_lazy('artist-list')
    success_message = "Исполнитель '%(name)s' был успешно создан"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message % form.instance.__dict__)
        return response

class ArtistUpdateView(SuccessMessageMixin, UpdateView):
    model = Artist
    template_name = 'qwerty/artist_form.html'
    fields = ['name', 'country', 'image']
    success_url = reverse_lazy('artist-list')
    success_message = "Исполнитель '%(name)s' был успешно обновлен"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message % form.instance.__dict__)
        return response

class ArtistDeleteView(SuccessMessageMixin, DeleteView):
    model = Artist
    template_name = 'qwerty/artist_confirm_delete.html'
    success_url = reverse_lazy('artist-list')
    success_message = "Исполнитель был успешно удален"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

# Аналогичные представления для жанров
class GenreListView(ListView):
    model = Genre
    template_name = 'qwerty/genre_list.html'
    context_object_name = 'genres'
    ordering = ['name']

class GenreDetailView(DetailView):
    model = Genre
    template_name = 'qwerty/genre_detail.html'
    context_object_name = 'genre'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = self.object.album_set.all()
        return context

class GenreCreateView(SuccessMessageMixin, CreateView):
    model = Genre
    template_name = 'qwerty/genre_form.html'
    fields = ['name', 'image']
    success_url = reverse_lazy('genre-list')
    success_message = "Жанр '%(name)s' был успешно создан"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message % form.instance.__dict__)
        return response

class GenreUpdateView(SuccessMessageMixin, UpdateView):
    model = Genre
    template_name = 'qwerty/genre_form.html'
    fields = ['name', 'image']
    success_url = reverse_lazy('genre-list')
    success_message = "Жанр '%(name)s' был успешно обновлен"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message % form.instance.__dict__)
        return response

class GenreDeleteView(SuccessMessageMixin, DeleteView):
    model = Genre
    template_name = 'qwerty/genre_confirm_delete.html'
    success_url = reverse_lazy('genre-list')
    success_message = "Жанр был успешно удален"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)