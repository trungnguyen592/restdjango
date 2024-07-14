from rest_framework import serializers
from .models import Item, StoryIventory, Supplier

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name')

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('id', 'name', 'contact_info')

class StoreInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryIventory
        fields = ('id','supplier', 'item',  'description', 'date_added')