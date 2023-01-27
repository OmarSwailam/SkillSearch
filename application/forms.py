from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile, Skill
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Full Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Password Confirmation'

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control mb-3', })
            field.label = ''
            field.help_text = None
            field.required = True

    def clean(self):
        super(CustomUserCreationForm, self).clean()
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if len(name) < 4:
            self._errors['name'] = self.error_class([
                'Minimum 4 characters required'])

        if len(name) > 50:
            self._errors['name'] = self.error_class([
                'You can use maximum of 50 characters'])

        emails = User.objects.values_list('email', flat=True)
        if email in emails:
            self._errors['email'] = self.error_class([
                'Email Already Exist'])

        try:
            validate_email(email)
        except ValidationError as e:
            self._errors['email'] = self.error_class([
                'Invalid Email'])

        if password1 != password2:
            self._errors['password2'] = self.error_class([
                'Passwords Does not match'])

        return self.cleaned_data


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user', )

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Full Name'
        self.fields['location'].widget.attrs['placeholder'] = 'Location'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['job_title'].widget.attrs['placeholder'] = 'Job Title'
        self.fields['bio'].widget.attrs['placeholder'] = 'Bio'
        self.fields['github_link'].widget.attrs['placeholder'] = 'Github'
        self.fields['linkedin_link'].widget.attrs['placeholder'] = 'Linkedin'
        self.fields['website_link'].widget.attrs['placeholder'] = 'Website'
        self.fields['twitter_link'].widget.attrs['placeholder'] = 'Twitter'
        self.fields['youtube_link'].widget.attrs['placeholder'] = 'Youtube'
        self.fields['social_link'].widget.attrs['placeholder'] = 'Social Media'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Phone number'

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control mb-3', })
            field.label = ''
            field.help_text = None
