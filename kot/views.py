from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class KOTMenuItemListView(generic.ListView):
    model = models.KOTMenuItem
    form_class = forms.KOTMenuItemForm


class KOTMenuItemCreateView(generic.CreateView):
    model = models.KOTMenuItem
    form_class = forms.KOTMenuItemForm


class KOTMenuItemDetailView(generic.DetailView):
    model = models.KOTMenuItem
    form_class = forms.KOTMenuItemForm


class KOTMenuItemUpdateView(generic.UpdateView):
    model = models.KOTMenuItem
    form_class = forms.KOTMenuItemForm
    pk_url_kwarg = "pk"


class KOTMenuItemDeleteView(generic.DeleteView):
    model = models.KOTMenuItem
    success_url = reverse_lazy("kot_KOTMenuItem_list")


class KOTStatusListView(generic.ListView):
    model = models.KOTStatus
    form_class = forms.KOTStatusForm


class KOTStatusCreateView(generic.CreateView):
    model = models.KOTStatus
    form_class = forms.KOTStatusForm


class KOTStatusDetailView(generic.DetailView):
    model = models.KOTStatus
    form_class = forms.KOTStatusForm


class KOTStatusUpdateView(generic.UpdateView):
    model = models.KOTStatus
    form_class = forms.KOTStatusForm
    pk_url_kwarg = "pk"


class KOTStatusDeleteView(generic.DeleteView):
    model = models.KOTStatus
    success_url = reverse_lazy("kot_KOTStatus_list")


class KOTListView(generic.ListView):
    model = models.KOT
    form_class = forms.KOTForm


class KOTCreateView(generic.CreateView):
    model = models.KOT
    form_class = forms.KOTForm


class KOTDetailView(generic.DetailView):
    model = models.KOT
    form_class = forms.KOTForm


class KOTUpdateView(generic.UpdateView):
    model = models.KOT
    form_class = forms.KOTForm
    pk_url_kwarg = "pk"


class KOTDeleteView(generic.DeleteView):
    model = models.KOT
    success_url = reverse_lazy("kot_KOT_list")


class OrderChannelListView(generic.ListView):
    model = models.OrderChannel
    form_class = forms.OrderChannelForm


class OrderChannelCreateView(generic.CreateView):
    model = models.OrderChannel
    form_class = forms.OrderChannelForm


class OrderChannelDetailView(generic.DetailView):
    model = models.OrderChannel
    form_class = forms.OrderChannelForm


class OrderChannelUpdateView(generic.UpdateView):
    model = models.OrderChannel
    form_class = forms.OrderChannelForm
    pk_url_kwarg = "pk"


class OrderChannelDeleteView(generic.DeleteView):
    model = models.OrderChannel
    success_url = reverse_lazy("kot_OrderChannel_list")
