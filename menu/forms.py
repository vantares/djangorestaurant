from django import forms
from menu.models import Category
from . import models


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = [
            "description",
            "name",
        ]


class ItemForm(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = [
            "item_category",
        ]

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields["item_category"].queryset = Category.objects.all()

