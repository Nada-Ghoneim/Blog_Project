from django import forms
from .models import Comment

class NewComment(forms.ModelForm):
    #message=forms.CharField(widget=forms.Textarea,max_length=4000)
    class Meta :
        model = Comment
        fields =['comment']
        #fields =['comment','message'] for coloumns not in comment table
