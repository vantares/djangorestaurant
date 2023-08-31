from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class KODListView(generic.ListView):
    model = models.KOD
    form_class = forms.KODForm


class KODCreateView(generic.CreateView):
    model = models.KOD
    form_class = forms.KODForm


class KODDetailView(generic.DetailView):
    model = models.KOD
    form_class = forms.KODForm


class KODUpdateView(generic.UpdateView):
    model = models.KOD
    form_class = forms.KODForm
    pk_url_kwarg = "pk"


class KODDeleteView(generic.DeleteView):
    model = models.KOD
    success_url = reverse_lazy("kod_KOD_list")


class StatusListView(generic.ListView):
    model = models.Status
    form_class = forms.StatusForm


class StatusCreateView(generic.CreateView):
    model = models.Status
    form_class = forms.StatusForm


class StatusDetailView(generic.DetailView):
    model = models.Status
    form_class = forms.StatusForm


class StatusUpdateView(generic.UpdateView):
    model = models.Status
    form_class = forms.StatusForm
    pk_url_kwarg = "pk"


class StatusDeleteView(generic.DeleteView):
    model = models.Status
    success_url = reverse_lazy("kod_Status_list")
