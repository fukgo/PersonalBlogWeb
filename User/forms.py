from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .models import Profile
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    code = forms.CharField(validators=[RegexValidator(regex='^.{5}$', message='验证码长度为5', code='nomatch')])
"""
code='nomatch'是一个自定义的错误代码。如果输入的 code 字段不符合要求，即不是4个字符长，验证器会产生一个错误，
错误消息为 'Length has to be 4'，同时这个错误会被标记为 'nomatch'，这样你就可以通过这个代码来识别这种特定类型的验证错误。"""
class RegisterForm(forms.ModelForm):
    password = forms.CharField()
    password_confirm = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError('密码输入不一致,请重试')
        return password_confirm


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'introduction', 'gender', 'birth_date')
        widgets = {
            'gender': forms.Select(attrs={'class': 'form-control', 'id': 'gender', 'name': 'gender'},
                                   choices=Profile.gender_choices),
        }

