from django.contrib import admin
from django import forms

from . import models


class CategoryAdminForm(forms.ModelForm):

    class Meta:
        model = models.Category
        fields = "__all__"


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
    list_display = [
        "description",
        "last_updated",
        "name",
        "created",
    ]
    readonly_fields = [
        "description",
        "last_updated",
        "name",
        "created",
    ]


class ItemAdminForm(forms.ModelForm):

    class Meta:
        model = models.Item
        fields = "__all__"


class ItemAdmin(admin.ModelAdmin):
    form = ItemAdminForm
    list_display = [
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Item, ItemAdmin)
