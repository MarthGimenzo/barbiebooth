from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        Majority of this code was copied from the instruction videos
        of Code Institute
        """
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'contactform'
            self.fields[field].widget.attrs['cols'] = 25
            if field == 'message':
                self.fields[field].widget.attrs['class'] = 'messagefield'
            self.fields[field].label = False
