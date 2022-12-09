from django import forms
from .models import *


class BlogForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control', 
            'placeholder': 'Title'
            }
        ))
    
    
    class Meta:
        model = BlogModel
        fields = ['title', 'content', 'image']
        
    def save (self, commit=True):
        blog_post = self.instance
        blog_post.title = self.cleaned_data['title']
        blog_post.content = self.cleaned_data['content']
        
        if self.cleaned_data['image']:
            blog_post.image = self.cleaned_data['image']
            
        if commit:
            blog_post.save
        return blog_post
        

class ReplyForm(forms.ModelForm):
    class Meta:
        model = CommentReply
        fields = ['reply']