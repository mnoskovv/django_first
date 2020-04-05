from django import forms
from django.contrib.auth.models import User
from users.models import Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    avatar = forms.ImageField(required=False, widget=forms.FileInput)
    class Meta:
        model = Profile
        fields = ('institution', 'avatar',)