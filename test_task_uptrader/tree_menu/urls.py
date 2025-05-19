from django.urls import path

from tree_menu import views


app_name = 'tree_menu'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path(
        '<str:item_name>/', views.MenuItemDetailView.as_view(),
        name='item_detail')]
