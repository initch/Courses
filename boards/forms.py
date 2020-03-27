from django.forms import ModelForm
from django import forms
from .models import Board


class NewBoardForm(ModelForm):
    topic = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.Textarea(attrs={'rows': 8, 'placeholder': 'Do you want to post a new topic now?'})
    )

    class Meta:
        model = Board
        fields = ['name', 'description', 'topic']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'placeholder': 'What a board it is?'})
        }
