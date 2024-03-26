from django.urls import path
from asset_management import views
from asset_management.models import LogMessage
from asset_management.models import Asset
# from django.contrib import admin

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],
    # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="asset_management/home.html",
)


asset_list_view = views.AssetListView.as_view(
    queryset=Asset.objects.order_by("id")[:5],
    context_object_name="message_list",
    template_name="asset_management/home.html",
)

urlpatterns = [
    # path("", views.home, name="home"),
    path("log/", views.log_message, name="log"),
    # path("admin/", admin.site.urls),
    path("", asset_list_view, name="home"),
    path("add-asset", views.add_asset, name="add-asset"),
    path('asset/<int:pk>/update/', views.AssetUpdateView.as_view(), name='asset-update'),  # Update view
]