import datetime
from django import forms
from django.db.models import TextField


    
class CommentForm(forms.Form):
    comment = forms.TextField(max_length=200, help_text='Enter a comment here')
