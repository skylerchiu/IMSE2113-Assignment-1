from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import redirect


from asset_management.forms import LogMessageForm
from asset_management.models import LogMessage

from asset_management.forms import AddAssetForm, AddUserForm
from asset_management.models import Asset, User

from django.views.generic import ListView, UpdateView

from random import randint

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage
    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

class AssetListView(ListView):
    model = Asset
    def get_context_data(self, **kwargs):
        context = super(AssetListView, self).get_context_data(**kwargs)
        return context
    
class AssetUpdateView(UpdateView):
    model = Asset
    fields = '__all__'  # Specify the fields you want to update
    template_name = 'asset_management/view-edit-asset.html'  # Template for updating
    success_url = '/'  # Redirect URL after successful update


    def get_object(self, queryset=None):
        # Fetch the product based on the pk from the URL
        return Asset.objects.get(pk=self.kwargs['pk'])
    
    def get_absolute_url(self):
        return ""
    
class UserListView(ListView):
    model = User
    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        return context
    
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
    

def add_user(request):
    form = AddUserForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
        return redirect("users")
    else:
        return render(request, "asset_management/add-asset.html", {"form": form})
    
