from django import forms
from .models import Community, Comment, Message

class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['title','content', 'img']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['to_user', 'from_user', 'message']