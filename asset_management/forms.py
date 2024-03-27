from django import forms
from asset_management.models import Asset
from django.contrib.auth.models import User

class UserAdminForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = '__all__'

class AssetAdminForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ("name", "description", 'registered_user')
