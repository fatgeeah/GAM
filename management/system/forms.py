from django import forms
from .models import Gamer

class GamerForm(forms.ModelForm):
   class Meta:
    model = Gamer
    fields = '__all__'
    labels = {
        'gamer_id': 'Gamer Id',
        'gamer_username': 'Gamer Username',
        'gamer_first_name' :'Gamer Firstname',
        'gamer_last_name' : 'Gamer Lastname',
        'email' : 'Email',
        'gamer_games' : 'Gamer Games',
    }
    widgets={
    'gamer_id': forms.NumberInput(attrs={'class':'form-control'}),
    'gamer_username' : forms.TextInput(attrs={'class' : 'form-control'}),
    'gamer_first_name' : forms.TextInput(attrs={'class' : 'form-control'}),
    'gamer_first_name' : forms.TextInput(attrs={'class' : 'form-control'}),
    'gamer_last_name' : forms.TextInput(attrs={'class' : 'form-control'}),
    'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
    'gamer_games' : forms.TextInput(attrs={'class' : 'form-control'}),
    }