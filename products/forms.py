from django.forms import ModelForm, Textarea
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        Majority of this code was copied from the instruction videos
        of Code Institute
        """
        super().__init__(*args, **kwargs)

        self.fields['description'].widget.attrs['autofocus'] = False
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'commentform'
            self.fields[field].label = False
        