from django import forms

from django.contrib.auth import authenticate, get_user_model, login, logout

from django.contrib.auth.models import User

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidateError('This user does not exists')
            if not user.check_password(password):
                raise forms.ValidateError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
    email1 = forms.Emailfield(label='Email Address')
    email2 = forms.Emailfield(label='Confirm email')
    password = forms.Charfields(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]
    def clean_email(self):
        email.self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exist():
            raise forms.ValidationError(
            "This email is already being used"
        )