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
    password = forms.CharField(widget=forms.PasswordInput)
    

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body",]