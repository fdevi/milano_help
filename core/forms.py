from django import forms
from django.contrib.auth.models import User
from .models import Profile

# Step 1: User base (username, email, password)
class RegistrationStep1Form(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Conferma Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        pw1 = cleaned_data.get('password1')
        pw2 = cleaned_data.get('password2')
        if pw1 and pw2 and pw1 != pw2:
            self.add_error('password2', "Le password non coincidono")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


# Step 2: Profile extra fields
class RegistrationStep2Form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birth_date', 'gender', 'phone', 'profile_photo']
