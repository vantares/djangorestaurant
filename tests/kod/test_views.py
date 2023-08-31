import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_KOD_list_view(client):
    instance1 = test_helpers.create_kod_KOD()
    instance2 = test_helpers.create_kod_KOD()
    url = reverse("kod_KOD_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_KOD_create_view(client):
    kod_nemu_item = test_helpers.create_menu_Item()
    kod_status = test_helpers.create_kod_Status()
    url = reverse("kod_KOD_create")
    data = {
        "staff_id": 1,
        "kod_nemu_item": kod_nemu_item.pk,
        "kod_status": kod_status.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_KOD_detail_view(client):
    instance = test_helpers.create_kod_KOD()
    url = reverse("kod_KOD_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_KOD_update_view(client):
    kod_nemu_item = test_helpers.create_menu_Item()
    kod_status = test_helpers.create_kod_Status()
    instance = test_helpers.create_kod_KOD()
    url = reverse("kod_KOD_update", args=[instance.pk, ])
    data = {
        "staff_id": 1,
        "kod_nemu_item": kod_nemu_item.pk,
        "kod_status": kod_status.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Status_list_view(client):
    instance1 = test_helpers.create_kod_Status()
    instance2 = test_helpers.create_kod_Status()
    url = reverse("kod_Status_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Status_create_view(client):
    url = reverse("kod_Status_create")
    data = {
        "status": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Status_detail_view(client):
    instance = test_helpers.create_kod_Status()
    url = reverse("kod_Status_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Status_update_view(client):
    instance = test_helpers.create_kod_Status()
    url = reverse("kod_Status_update", args=[instance.pk, ])
    data = {
        "status": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302
