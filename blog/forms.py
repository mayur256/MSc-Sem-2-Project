from django import forms
from django.forms import ModelForm,TextInput,EmailInput,ModelChoiceField,MultiValueField,Textarea,SelectMultiple,FileInput
from .models import Post, Profile, Comment,Report
from django.contrib.auth.models import User
class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'body',
            'status',
            'restrict_comment',
        )
        widgets={'title':TextInput(attrs={'class':"form-control",'required':"true"}),
        'body':Textarea(attrs={'class':"form-control",'required':"true"}),
        }
class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'body',
            'status',
            'restrict_comment',
        )
        widgets={'title':TextInput(attrs={'class':"form-control",'required':"true"}),
        'body':Textarea(attrs={'class':"form-control",'required':"true"}),
        }
class UserLoginForm(forms.Form):
    username = forms.CharField(label="",widget=forms.TextInput(attrs={'class': "form-control",'placeholder':"Enter Your UserName"}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': "form-control",'placeholder':"Enter Your Password  "}))
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'class': "form-control"}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs = {'class': "form-control"}))
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )
        widgets={'username':TextInput(attrs={'class':"form-control",'required':"true"}),
        'first_name':TextInput(attrs={'class':"form-control",'required':"true"}),
        'last_name':TextInput(attrs={'class':"form-control",'required':"true"}),
        'email':EmailInput(attrs={'class':"form-control",'required':"true"}),
        }
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Password Mismatch")
        return confirm_password
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )
        widgets={'username':TextInput(attrs={'class':"form-control",'readonly':'readonly'}),
        'first_name':TextInput(attrs={'class':"form-control",}),
        'last_name':TextInput(attrs={'class':"form-control",}),
        'email':EmailInput(attrs={'class':"form-control",'readonly':'readonly'}),
        }
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
        widgets={'dob':TextInput(attrs={'type':'date','class':"form-control",}),
        'mob':TextInput(attrs={'type':'number','class':"form-control",}),
        'city':TextInput(attrs={'type':'text','class':"form-control",}),
        'photo':FileInput(attrs={'class':"form-control",'accept':'image/*'}),
        }
class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.TextInput(attrs={'id':'text','class': 'form-control', 'placeholder': 'Text goes here!!!'}))
    class Meta:
        model = Comment
        fields = ('content',)

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = (
            'reason',
            'body',
        )
        widgets={
        'body':TextInput(attrs={'class':"form-control",}),
        }