__author__ = 'libingxin'
from django import forms
from .models import Post
from django.contrib.admin import widgets


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('title', 'text',)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'published_date')
        widgets = {
            'title': forms.TextInput(attrs={'size': '50'}),
            'text': forms.Textarea(attrs={'class': 'melody', 'size': '10', 'placeholder': 'I am a text'}, ),
            'published_date': forms.DateInput(attrs={'class': 'vDateField', 'value': '2011-01-01'}),
        }

#     # def __init__(self, *args, **kwargs):
#     #     super(PostForm, self).__init__(*args, **kwargs)
#     #     self.fields['title'].widget = forms.TextInput({'class': 'form-control'})
#     #     # self.fields['text'].widget = forms.CharField({'class': 'form-control'})
#
#

