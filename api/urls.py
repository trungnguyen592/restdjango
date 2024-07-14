from django.urls import path
from . import views

urlpatterns = [
    #Urls for items
    path('items/', views.ItemListCreateAPIView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', views.ItemRetrieveUpdateDestroyAPIView.as_view(), name='item-detail'),

    # urls for suppliers
    path('suppliers/', views.SupplierListCreateAPIView.as_view(), name='supplier-list-create'),
    path('suppliers/<int:pk>/', views.SupplierRetrieveUpdateDestroyAPIView.as_view(), name='supplier-detail'),

    # urls for store inventory
    path('storeinventory/', views.StoreInventoryListCreateAPIView.as_view(), 
         name='storeinventory-list-create'),
    path('storeinventory/<int:pk>/', views.StoreInventoryRetrieveUpdateDestroyAPIView.as_view(), 
         name='storeinventory-detail'),

]