# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from custom_users.models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserCreationForm(forms.ModelForm):
    REQUIRED_FIELDS = ['email', 'password1', 'password2']
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CustomUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label= ("Password"),
        help_text= ("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"password/\">this form</a>."))

    class Meta:
        model = CustomUser
        fields = ('username',)

    def clean_password(self):
        return self.initial["password"]


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ('email',)
    filter_horizontal = ('groups', 'user_permissions')
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': tuple()}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2',)}
        ),
    )
    
admin.site.register(CustomUser, CustomUserAdmin)