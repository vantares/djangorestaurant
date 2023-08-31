from django.db import models
from django.urls import reverse


class Category(models.Model):

    # Fields
    description = models.CharField(max_length=200)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("menu_Category_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("menu_Category_update", args=(self.pk,))



class Item(models.Model):

    # Relationships
    item_category = models.ForeignKey("menu.Category", on_delete=models.DO_NOTHING)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("menu_Item_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("menu_Item_update", args=(self.pk,))

