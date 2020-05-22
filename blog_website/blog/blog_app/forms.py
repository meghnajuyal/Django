from django import forms
from blog_app.models import BlogPost,Comment


class PostForm(forms.ModelForm):
    class Meta():
        model=BlogPost
        fields=('author','title','text')

        widgets={'title':forms.TextInput(attrs={'class': 'textinputclass'}),
                  'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
                  }


class CommentForm(forms.ModelForm):
    class Meta():
        model=Comment
        fields=('author','text')

        widgets={
                 'author':forms.TextInput(attrs={'class':'texinputclass'}),
                  'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
