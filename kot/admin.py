from django.contrib import admin
from django import forms

from . import models


class KOTMenuItemAdminForm(forms.ModelForm):

    class Meta:
        model = models.KOTMenuItem
        fields = "__all__"


class KOTMenuItemAdmin(admin.ModelAdmin):
    form = KOTMenuItemAdminForm
    list_display = [
        "last_updated",
        "quantity",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "quantity",
        "created",
    ]


class KOTStatusAdminForm(forms.ModelForm):

    class Meta:
        model = models.KOTStatus
        fields = "__all__"


class KOTStatusAdmin(admin.ModelAdmin):
    form = KOTStatusAdminForm
    list_display = [
        "status",
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "status",
        "last_updated",
        "created",
    ]


class KOTAdminForm(forms.ModelForm):

    class Meta:
        model = models.KOT
        fields = "__all__"


class KOTAdmin(admin.ModelAdmin):
    form = KOTAdminForm
    list_display = [
        "last_updated",
        "staff_id",
        "out_time",
        "created",
        "in_time",
    ]
    readonly_fields = [
        "last_updated",
        "staff_id",
        "out_time",
        "created",
        "in_time",
    ]


class OrderChannelAdminForm(forms.ModelForm):

    class Meta:
        model = models.OrderChannel
        fields = "__all__"


class OrderChannelAdmin(admin.ModelAdmin):
    form = OrderChannelAdminForm
    list_display = [
        "name",
        "created",
        "last_updated",
        "close_time",
        "open_time",
        "description",
    ]
    readonly_fields = [
        "name",
        "created",
        "last_updated",
        "close_time",
        "open_time",
        "description",
    ]


admin.site.register(models.KOTMenuItem, KOTMenuItemAdmin)
admin.site.register(models.KOTStatus, KOTStatusAdmin)
admin.site.register(models.KOT, KOTAdmin)
admin.site.register(models.OrderChannel, OrderChannelAdmin)
