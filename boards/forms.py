from django.forms import ModelForm
from django import forms
from .models import Board, Topic


class NewBoardForm(ModelForm):
    topic = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.Textarea(attrs={'rows': 8, 'placeholder': 'Do you want to post a new topic now?'})
    )
    course = forms.CharField(
        max_length=40,
        required=False,
        help_text='The course isn\'t exists!'
    )

    class Meta:
        model = Board
        fields = ['name', 'description', 'course', 'topic']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'placeholder': 'What a board it is?'})
        }


class NewTopicForm(ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'What is on your mind?'}),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']
