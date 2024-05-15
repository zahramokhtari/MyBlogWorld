from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'type']
        widgets = {
            'type': forms.Select(attrs={'id': 'id_type'}),  # Ensure the city field has this ID
        }
