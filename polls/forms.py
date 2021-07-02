
from django.forms import ModelForm
from django.forms.widgets import Widget
from .models import Comments, Question
from django import forms


class CommentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your name'}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    body = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Comments
        fields = ('name', 'email', 'body')
