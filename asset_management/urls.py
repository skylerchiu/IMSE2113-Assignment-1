from django.urls import path, include
from asset_management import views
from asset_management.models import LogMessage
from asset_management.models import Asset
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import admin


def redirect_to_login(request):
    return HttpResponseRedirect('login/')



asset_list_view = login_required(views.AssetListView.as_view(
    context_object_name="message_list",
    template_name="asset_management/home.html",
))

urlpatterns = [
    path('', redirect_to_login),
    path('password_change/', views.ChangePasswordView.as_view(), name='password_change'),
    path('edit-profile', views.ProfileEditView.as_view(), name='edit-profile'),
    path("admin/", admin.site.urls),
    path("", include("django.contrib.auth.urls")), 
    path("home", asset_list_view, name="home"),
    path('asset/<int:pk>/update/', views.AssetUpdateView.as_view(), name='asset-update'),  # Update view

]