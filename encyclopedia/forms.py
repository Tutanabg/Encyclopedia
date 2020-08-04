from django import forms 
from Post.models import Post 
class EditEntryForm(forms.ModelForm): 
         class Meta: 
             model = Post
             fields = __all__
