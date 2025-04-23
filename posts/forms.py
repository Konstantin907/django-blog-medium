from django import forms
from .models import Post, Comment
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'image', 'body', 'category']
        widgets = {
            'category': forms.Select(attrs={'class': 'w-full mt-1 p-2 border rounded'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Write your comment here...',
                'class': 'w-full p-2 border border-gray-300 rounded-lg text-sm'
            }),
        }
