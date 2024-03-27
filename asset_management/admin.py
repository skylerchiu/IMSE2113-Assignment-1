from django.contrib import admin
from asset_management.models import Asset
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

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

from django.contrib.auth.models import User

admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    readonly_fields = ('date_joined', 'last_login')
    form = UserAdminForm

# Register your models here.
@admin.register(Asset)
class Asset(admin.ModelAdmin):
    list_display = ("name", "description", 'assigned', 'registered_user', 'checkout_date')
    readonly_fields = ('checkout_date', 'id')
    form = AssetAdminForm
    pass


admin.site.site_header = 'Asset Management Admin'