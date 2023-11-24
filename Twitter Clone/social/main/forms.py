from django import forms
from .models import Meep, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class ProfilePicForm(forms.ModelForm):
    profile_image = forms.ImageField(label="პროფილის ფოტო")
    profile_bio = forms.CharField(label='', widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'თქვენი ბიო...'}))
    facebook_link = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Facebook Link'}))
    instagram_link = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Instagram Link'}))
    github_link = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'GitHub Link'}))
    linkedin_link = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'LinkedIn Link'}))

    class Meta:
        model = Profile
        fields = ('profile_image', 'profile_bio', 'facebook_link', 'instagram_link', 'github_link', 'linkedin_link', )


class MeepForm(forms.ModelForm):
    body = forms.CharField(required=True,
                           widget=forms.widgets.Textarea(
                                attrs={
                                    "placeholder":'დაწერეთ პოსტი...',
                                    "class":'form-control',

                                }
                                ),
                                label='',
                           )
    
    class Meta:
        model = Meep
        exclude = ("user", "likes", )

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'თქვენი იმეილი...'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'თქვენი სახელი...'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'თქვენი გვარი...'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'თქვენი ნიქნეიმი'
		self.fields['username'].label = ''
	
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'თქვენი პაროლი'
		self.fields['password1'].label = ''

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'გაიმეორეთ პაროლი'
		self.fields['password2'].label = ''