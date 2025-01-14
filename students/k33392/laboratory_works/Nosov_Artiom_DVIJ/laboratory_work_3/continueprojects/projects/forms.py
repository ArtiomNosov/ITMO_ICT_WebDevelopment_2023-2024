from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User 
from django import forms

# class StudentSkillsForm(forms.Form):
    # Поля формы
    # skill = forms.Ma # CharField(label='example_lable', max_length=100)

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']
    pass


# class JobForm(ModelForm): # TODO
#     class Meta:
#         model = Job
#         fields = ['name', 'description', 'topic', 'cost']
#         exclude = []
#         widgets = {
#             'cost' : forms.TextInput(attrs = {'placeholder': '1000 руб'}),
#         }
        
        
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']
        widgets = {
            'avatar': forms.TextInput(attrs={'placeholder': 'аватар', "title": "аватар"}),
            'name': forms.TextInput(attrs={'placeholder': 'имя', "title": "имя"}),
            'username': forms.TextInput(attrs={'placeholder': 'логин', "title": "логин"}),
            'bio': forms.TextInput(attrs={'placeholder': 'био', "title": "био"}),
        }
