from django import forms
from menu.models import Item
from kod.models import Status
from . import models


class KODForm(forms.ModelForm):
    class Meta:
        model = models.KOD
        fields = [
            "staff_id",
            "kod_nemu_item",
            "kod_status",
        ]

    def __init__(self, *args, **kwargs):
        super(KODForm, self).__init__(*args, **kwargs)
        self.fields["kod_nemu_item"].queryset = Item.objects.all()
        self.fields["kod_status"].queryset = Status.objects.all()



class StatusForm(forms.ModelForm):
    class Meta:
        model = models.Status
        fields = [
            "status",
        ]
