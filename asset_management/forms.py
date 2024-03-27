# hello.forms.py
from django import forms
from asset_management.models import LogMessage
from asset_management.models import Asset
from django.contrib.auth.models import User
class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",) # NOTE: the trailing comma is required


class AddAssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ("name", "description")
