from django import forms
from .models import employer , materiaux ,holidays
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class LoginUserForm(forms.Form):
    username=forms.CharField( label='', max_length=50 , initial=None, widget=forms.TextInput(attrs={"class" : "username" , "placeholder" : 'username' , 'required' : True ,  'title':"Please enter your username"} ))
    password=forms.CharField( initial=None,widget=forms.PasswordInput( attrs={'class' : 'password' , 'placeholder' : 'password'}) , label='')

class employerform(forms.ModelForm):
    direct=[
    ('DT','DT'),
    ('DTE','DTE'),
    ('PAC','PAC'),
    ('DAF','DAF'),
    ]
    cate=[
        ('admin','admin'),
        ('directeur','directeur'),
        ('chef labo','chef labo'),
        ('operateur','operateur'),
        ('reception','reception'),
    ]
    
    photo=forms.ImageField(label='',required=False   , widget=forms.ClearableFileInput(attrs={'class': 'image_input' }))
    categorie=forms.ChoiceField(label='categorie',choices=cate , widget=forms.Select( attrs={'class': 'select_input' , 'placeholder' : 'categorie'}))
    direction=forms.ChoiceField(label='direction', choices=direct  , widget=forms.Select(attrs={'class': 'select_input' , 'placeholder' : 'direction'}))
    class Meta:
        model = employer
        fields = ['photo' , 'categorie' , 'direction']

class userform(forms.ModelForm):
    class Meta:
        model=User
        fields= ['username' , 'first_name' , 'last_name' , 'password1' , 'password2']
    username=forms.CharField(label='' , widget=forms.TextInput(attrs={'placeholder' : 'username' , 'class' : 'text_input'}))
    first_name=forms.CharField( label='',widget=forms.TextInput(attrs={'placeholder' : 'first name' , 'class' : 'text_input'}))
    last_name=forms.CharField( label='', widget=forms.TextInput(attrs={'placeholder' : 'last name' , 'class' : 'text_input'}))
    password1=forms.CharField(label='' , widget=forms.PasswordInput(attrs={'placeholder' : 'password' , 'class' : 'text_input'}))
    password2=forms.CharField(label='' , widget=forms.PasswordInput(attrs={'placeholder' : 'password confirmation' , 'class' : 'text_input'}))
    
    
class materiauxform(forms.ModelForm):
    class Meta:
        model = materiaux
        fields = ['type' ,'nom' ,'delai']


class holidaysform(forms.ModelForm):
    occasion=forms.CharField(label='' , widget=forms.TextInput(attrs={'class':'occasion' , 'placeholder':'occasion' }))
    first_day=forms.CharField(label='' , widget=forms.TextInput(attrs={'class':'h_date' ,'id':'start' , 'placeholder':'date debut','readonly':'readonly'}))
    last_day=forms.CharField(label='' , widget=forms.TextInput(attrs={'class':'h_date' , 'id':'end' ,'placeholder':'date fin','readonly':'readonly'}))
    days_number=forms.CharField(label='' , widget=forms.TextInput(attrs={'class':'days_namber' , 'placeholder':'nombre des jours','readonly':'readonly'}))
    class Meta:
        model = holidays
        fields = [ 'occasion' ,'first_day' , 'last_day'  , 'days_number']