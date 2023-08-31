import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_Category_list_view(client):
    instance1 = test_helpers.create_menu_Category()
    instance2 = test_helpers.create_menu_Category()
    url = reverse("menu_Category_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Category_create_view(client):
    url = reverse("menu_Category_create")
    data = {
        "description": "text",
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Category_detail_view(client):
    instance = test_helpers.create_menu_Category()
    url = reverse("menu_Category_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Category_update_view(client):
    instance = test_helpers.create_menu_Category()
    url = reverse("menu_Category_update", args=[instance.pk, ])
    data = {
        "description": "text",
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Item_list_view(client):
    instance1 = test_helpers.create_menu_Item()
    instance2 = test_helpers.create_menu_Item()
    url = reverse("menu_Item_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Item_create_view(client):
    item_category = test_helpers.create_menu_Category()
    url = reverse("menu_Item_create")
    data = {
        "item_category": item_category.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Item_detail_view(client):
    instance = test_helpers.create_menu_Item()
    url = reverse("menu_Item_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Item_update_view(client):
    item_category = test_helpers.create_menu_Category()
    instance = test_helpers.create_menu_Item()
    url = reverse("menu_Item_update", args=[instance.pk, ])
    data = {
        "item_category": item_category.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
