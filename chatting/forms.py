from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    to = forms.CharField(label='받는사람', max_length=1000, 
        widget=forms.Textarea(attrs={'rows':'1', 'cols': '50'}))
    body = forms.CharField(label='내용', max_length=1000, 
        widget=forms.Textarea(attrs={'rows':'15', 'cols': '50'}))
    class Meta:
        model = Message
        fields =['to','body']


