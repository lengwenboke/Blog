from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'text']


class LsmgForm(forms.ModelForm):
    class Meta:
        model = Lmsg
        fields = ['name', 'email', 'text']


class FriendlyForm(forms.ModelForm):
    class Meta:
        model = Friendly
        fields = ['title', 'weburl', 'email', 'desc', 'reason']
