from django.db import models
from django.urls import reverse


class KOTMenuItem(models.Model):

    # Relationships
    menu_item = models.ForeignKey("menu.Item", on_delete=models.CASCADE)
    kot = models.ForeignKey("kot.KOT", on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("kot_KOTMenuItem_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("kot_KOTMenuItem_update", args=(self.pk,))



class KOTStatus(models.Model):

    # Fields
    status = models.CharField(max_length=20)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("kot_KOTStatus_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("kot_KOTStatus_update", args=(self.pk,))



class KOT(models.Model):

    # Relationships
    status = models.ForeignKey("kot.KOTStatus", on_delete=models.CASCADE)
    order_channel = models.ForeignKey("kot.OrderChannel", on_delete=models. DO_NOTHING)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    staff_id = models.PositiveIntegerField()
    out_time = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    in_time = models.DateTimeField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("kot_KOT_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("kot_KOT_update", args=(self.pk,))



class OrderChannel(models.Model):

    # Fields
    name = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    close_time = models.DateTimeField()
    open_time = models.DateTimeField()
    description = models.CharField(max_length=200)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("kot_OrderChannel_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("kot_OrderChannel_update", args=(self.pk,))

