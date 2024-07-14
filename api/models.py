from django.db import models
from django.utils import timezone


class Item(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class StoryIventory(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    description = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.item.name} from {self.supplier.name}"