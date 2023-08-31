from django.db import models
from django.urls import reverse


class KOD(models.Model):

    # Relationships
    kod_nemu_item = models.ForeignKey("menu.Item", on_delete=models.CASCADE)
    kod_status = models.ForeignKey("kod.Status", on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    staff_id = models.PositiveIntegerField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("kod_KOD_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("kod_KOD_update", args=(self.pk,))



class Status(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    status = models.CharField(max_length=20)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("kod_Status_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("kod_Status_update", args=(self.pk,))

