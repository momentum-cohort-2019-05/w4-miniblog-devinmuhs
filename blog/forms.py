import datetime
from django import forms
from django.db.models import TextField
from .models import BlogPost, Comment

    
# class CommentForm(forms.Form):
#     comment = forms.CharField(max_length=200, help_text='Enter a comment here')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'comment')