'''
Created on Jan 14, 2013

@author: surecc
'''
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='Your E-mail address')
    message = forms.CharField(widget=forms.Textarea)
    
    # start as clean_ and end as the name of the words, it will valide in auto
    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError('Not enough words!')
        return message
    