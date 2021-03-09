from django.urls import path
from . import views

app_name = 'show_products'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.ItemDetail.as_view(), name='detail'),
    path('add', views.CreateItem.as_view(), name='add_item'),
    path('update/<int:item_id>/', views.update_item, name='update_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]
