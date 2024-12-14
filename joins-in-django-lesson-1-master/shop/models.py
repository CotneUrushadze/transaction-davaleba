from django.db import models
from django.db.models import Count


class CategoryManager(models.Manager):
    def with_item_count(self, *args, **kwargs):
        item_count = self.get_queryset().annotate(item_count = Count('items'))
        for category in item_count:
            print(f"Category: {category.name}, Item count: {category.item_count}")


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    objects = CategoryManager()

    def __str__(self):
        return self.name
    




class ItemManager(models.Manager):
    def with_tag_count(self, *args, **kwargs):
        tags_count = self.get_queryset().annotate(tags_count = Count('tags'))
        for item in tags_count:
            print(f"Item: {item.name}, tag count: {item.tags_count}")


class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    objects = ItemManager()

    def __str__(self):
        return self.name





class TagManager(models.Manager):
    def popular_tags(self, min_items):
        item_quantity = self.annotate(item_quantity = Count('items')).filter(item_quantity__gt=min_items)
        for tag in item_quantity:
            print(f"tag: {tag.name}, item quantity : {tag.item_quantity}")


class Tag(models.Model):
    name = models.CharField(max_length=50)
    items = models.ManyToManyField(Item, related_name='tags', blank=True)
    objects = TagManager()

    def __str__(self):
        return self.name
