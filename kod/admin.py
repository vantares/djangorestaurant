from django.contrib import admin
from django import forms

from . import models


class KODAdminForm(forms.ModelForm):

    class Meta:
        model = models.KOD
        fields = "__all__"


class KODAdmin(admin.ModelAdmin):
    form = KODAdminForm
    list_display = [
        "last_updated",
        "created",
        "staff_id",
    ]
    readonly_fields = [
        "last_updated",
        "created",
        "staff_id",
    ]


class StatusAdminForm(forms.ModelForm):

    class Meta:
        model = models.Status
        fields = "__all__"


class StatusAdmin(admin.ModelAdmin):
    form = StatusAdminForm
    list_display = [
        "created",
        "last_updated",
        "status",
    ]
    readonly_fields = [
        "created",
        "last_updated",
        "status",
    ]


admin.site.register(models.KOD, KODAdmin)
admin.site.register(models.Status, StatusAdmin)
