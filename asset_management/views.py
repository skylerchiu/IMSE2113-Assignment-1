from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import redirect


from asset_management.forms import LogMessageForm
from asset_management.models import LogMessage

from asset_management.forms import AddAssetForm
from asset_management.models import Asset

from django.views.generic import ListView, UpdateView

from random import randint
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView

    
class AssetListView(ListView):
    model = Asset
    def get_queryset(self):
        # Only include Assets where 'registered_user' is the current user
        return super().get_queryset().filter(registered_user=self.request.user)
    
class AssetUpdateView(UpdateView):
    model = Asset
    fields = '__all__'  # Specify the fields you want to update
    template_name = 'asset_management/view-edit-asset.html'  # Template for updating
    success_url = '/home'  # Redirect URL after successful update


    def get_object(self, queryset=None):
        # Fetch the product based on the pk from the URL
        return Asset.objects.get(pk=self.kwargs['pk'])
    
    def get_absolute_url(self):
        return ""
    
def hello_there(request, name):
    return render(
    request,
    'asset_management/home.html',
    {
    'name': name,
    'date': datetime.now()
    }
 )


def log_message(request):
    form = LogMessageForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
        return redirect("")
    else:
        return render(request, "asset_management/log_message.html", {"form": form})
    

def add_asset(request):
    form = AddAssetForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.checkout_date = datetime.now()
            message.barcode = str(randint(0, 1000000000))
            message.save()
        return redirect("home")
    else:
        return render(request, "asset_management/add-asset.html", {"form": form})
    

class ChangePasswordView(PasswordChangeView):
    template_name = 'registration/password_change.html'
    success_url = '/'


class ProfileEditView(UpdateView):
    model = User
    fields = ('username', 'first_name', 'last_name', 'email')  # Specify the fields you want to update
    template_name = 'asset_management/edit-profile.html'  # Template for updating
    success_url = '/home'  # Redirect URL after successful update


    def get_object(self, queryset=None):
        # Fetch the product based on the pk from the URL
        return super().get_queryset().filter(username=self.request.user).first()
    
    def get_absolute_url(self):
        return ""
    
