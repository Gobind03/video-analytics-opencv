from django import forms


class LoginForm(forms.Form):
    submit_url = '/accounts/do_login'
    username = forms.CharField(label='Username',
                               max_length=255,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Enter Username Here'}))
    password = forms.CharField(label='Password',
                               max_length=255,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': '********'}))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
