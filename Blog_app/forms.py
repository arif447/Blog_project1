from django.forms import ModelForm
from django import forms
from Blog_app.models import Blog, Comment, Like

class Comment_Form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
