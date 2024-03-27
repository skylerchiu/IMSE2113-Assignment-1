from asset_management.models import Asset

from django.views.generic import ListView, UpdateView

from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView

    
class AssetListView(ListView):
    model = Asset
    def get_queryset(self):
        return super().get_queryset().filter(registered_user=self.request.user)
    

class AssetUpdateView(UpdateView):
    model = Asset
    fields = '__all__'
    template_name = 'asset_management/view-edit-asset.html'
    success_url = '/home'

    def get_object(self, queryset=None):
        return Asset.objects.get(pk=self.kwargs['pk'])
    
    def get_absolute_url(self):
        return ""


class ChangePasswordView(PasswordChangeView):
    template_name = 'registration/password_change.html'
    success_url = '/'


class ProfileEditView(UpdateView):
    model = User
    fields = ('username', 'first_name', 'last_name', 'email')
    template_name = 'asset_management/edit-profile.html'
    success_url = '/home'  

    def get_object(self, queryset=None):
        return super().get_queryset().filter(username=self.request.user).first()
    
    def get_absolute_url(self):
        return ""
    
