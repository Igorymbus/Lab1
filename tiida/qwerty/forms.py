from django import forms
from .models import Album, Artist, Genre

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'release_date', 'price', 'label', 'genre', 'artists', 'cover_image']

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'country', 'image']

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name', 'image'] 