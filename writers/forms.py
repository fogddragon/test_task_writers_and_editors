from django import forms

from writers.models import User


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(max_length=20)
    password2 = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'role', 'password2', 'password1',]

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        if cleaned_data['password1'] != cleaned_data['password2']:
            self.add_error('password1', 'Passwords must match.')
        else:
            self.cleaned_data['password'] = cleaned_data['password1']
            self.cleaned_data.pop('password1')
            self.cleaned_data.pop('password2')
        return self.cleaned_data



class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'role',]
