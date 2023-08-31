from django import forms
from menu.models import Item
from kot.models import KOT
from kot.models import KOTStatus
from kot.models import OrderChannel
from . import models


class KOTMenuItemForm(forms.ModelForm):
    class Meta:
        model = models.KOTMenuItem
        fields = [
            "quantity",
            "menu_item",
            "kot",
        ]

    def __init__(self, *args, **kwargs):
        super(KOTMenuItemForm, self).__init__(*args, **kwargs)
        self.fields["menu_item"].queryset = Item.objects.all()
        self.fields["kot"].queryset = KOT.objects.all()



class KOTStatusForm(forms.ModelForm):
    class Meta:
        model = models.KOTStatus
        fields = [
            "status",
        ]


class KOTForm(forms.ModelForm):
    class Meta:
        model = models.KOT
        fields = [
            "staff_id",
            "out_time",
            "in_time",
            "status",
            "order_channel",
        ]

    def __init__(self, *args, **kwargs):
        super(KOTForm, self).__init__(*args, **kwargs)
        self.fields["status"].queryset = KOTStatus.objects.all()
        self.fields["order_channel"].queryset = OrderChannel.objects.all()



class OrderChannelForm(forms.ModelForm):
    class Meta:
        model = models.OrderChannel
        fields = [
            "name",
            "close_time",
            "open_time",
            "description",
        ]
