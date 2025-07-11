from django import forms
from django.core import validators


def validate_age(value):
    if value % 2 != 0:
        raise forms.ValidationError("Число должно быть четным")

class TestForm(forms.Form):
    name = forms.CharField(max_length=15, label="Имя")
    bio = forms.CharField(
        widget=forms.Textarea,
          required=False,
            validators=[validators.MaxLengthValidator(15), validators.MinLengthValidator(4)]
    )
    email = forms.EmailField()
    age = forms.IntegerField(validators=[validate_age])
    is_active = forms.BooleanField()
    password1 = forms.CharField(widget=forms.PasswordInput, label="Придумайте пароль")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Подтвердите пароль")
    

    def clean_email(self):
        email = self.cleaned_data["email"]
        if "gmail.com" not in email:
            raise forms.ValidationError("Only Gmail")
        return email

    def clean(self):
        cleaned_data = super().clean()
        pass1 = cleaned_data["password1"]
        pass2 = cleaned_data["password2"]

        if pass1 != pass2:
            # self.add_error("password2", "Passwords didn't match")
            raise forms.ValidationError("Пароли должны совпадать")
        return cleaned_data


from .models import Post

class PostModeForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body",]


class PostForm(forms.Form):
    title = forms.CharField(max_length=200)
    body = forms.CharField(widget=forms.Textarea())