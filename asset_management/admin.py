from django.contrib import admin
from asset_management.models import Asset
from django import forms
from django.contrib.auth.models import User


class AssetAdminForm(forms.ModelForm):
    reigstered_user = forms.ModelChoiceField(queryset=User.objects.all())
    class Meta:
        model = Asset
        fields = "__all__"



# Register your models here.
@admin.register(Asset)
class Asset(admin.ModelAdmin):
    list_display = ("name", "description")
    form = AssetAdminForm
    
    pass


