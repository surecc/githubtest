'''
Created on Jan 15, 2013

@author: surecc
'''
from django import forms

class SoupForm(forms.Form):
    LIST_WEBSITE = (
                    ('360buy','360buy'),
                    ('taobao','taobao'),
                    ('others','others'),
                    )
    url = forms.CharField(widget=forms.Textarea)
    website = forms.ChoiceField(choices=LIST_WEBSITE, required=True)
    level = forms.IntegerField(required=False)
    
    # start as clean_ and end as the name of the words, it will valide in auto
    '''
    def clean_url(self):
        url = self.cleaned_data['url']
        num_words = len(url.split())
        if num_words < 10:
            raise forms.ValidationError(num_words)
        return url'''
    