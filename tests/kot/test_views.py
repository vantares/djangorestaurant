import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_KOTMenuItem_list_view(client):
    instance1 = test_helpers.create_kot_KOTMenuItem()
    instance2 = test_helpers.create_kot_KOTMenuItem()
    url = reverse("kot_KOTMenuItem_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_KOTMenuItem_create_view(client):
    menu_item = test_helpers.create_menu_Item()
    kot = test_helpers.create_kot_KOT()
    url = reverse("kot_KOTMenuItem_create")
    data = {
        "quantity": 1,
        "menu_item": menu_item.pk,
        "kot": kot.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_KOTMenuItem_detail_view(client):
    instance = test_helpers.create_kot_KOTMenuItem()
    url = reverse("kot_KOTMenuItem_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_KOTMenuItem_update_view(client):
    menu_item = test_helpers.create_menu_Item()
    kot = test_helpers.create_kot_KOT()
    instance = test_helpers.create_kot_KOTMenuItem()
    url = reverse("kot_KOTMenuItem_update", args=[instance.pk, ])
    data = {
        "quantity": 1,
        "menu_item": menu_item.pk,
        "kot": kot.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_KOTStatus_list_view(client):
    instance1 = test_helpers.create_kot_KOTStatus()
    instance2 = test_helpers.create_kot_KOTStatus()
    url = reverse("kot_KOTStatus_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_KOTStatus_create_view(client):
    url = reverse("kot_KOTStatus_create")
    data = {
        "status": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_KOTStatus_detail_view(client):
    instance = test_helpers.create_kot_KOTStatus()
    url = reverse("kot_KOTStatus_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_KOTStatus_update_view(client):
    instance = test_helpers.create_kot_KOTStatus()
    url = reverse("kot_KOTStatus_update", args=[instance.pk, ])
    data = {
        "status": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_KOT_list_view(client):
    instance1 = test_helpers.create_kot_KOT()
    instance2 = test_helpers.create_kot_KOT()
    url = reverse("kot_KOT_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_KOT_create_view(client):
    status = test_helpers.create_kot_KOTStatus()
    order_channel = test_helpers.create_kot_OrderChannel()
    url = reverse("kot_KOT_create")
    data = {
        "staff_id": 1,
        "out_time": datetime.now(),
        "in_time": datetime.now(),
        "status": status.pk,
        "order_channel": order_channel.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_KOT_detail_view(client):
    instance = test_helpers.create_kot_KOT()
    url = reverse("kot_KOT_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_KOT_update_view(client):
    status = test_helpers.create_kot_KOTStatus()
    order_channel = test_helpers.create_kot_OrderChannel()
    instance = test_helpers.create_kot_KOT()
    url = reverse("kot_KOT_update", args=[instance.pk, ])
    data = {
        "staff_id": 1,
        "out_time": datetime.now(),
        "in_time": datetime.now(),
        "status": status.pk,
        "order_channel": order_channel.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_OrderChannel_list_view(client):
    instance1 = test_helpers.create_kot_OrderChannel()
    instance2 = test_helpers.create_kot_OrderChannel()
    url = reverse("kot_OrderChannel_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_OrderChannel_create_view(client):
    url = reverse("kot_OrderChannel_create")
    data = {
        "name": "text",
        "close_time": datetime.now(),
        "open_time": datetime.now(),
        "description": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_OrderChannel_detail_view(client):
    instance = test_helpers.create_kot_OrderChannel()
    url = reverse("kot_OrderChannel_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_OrderChannel_update_view(client):
    instance = test_helpers.create_kot_OrderChannel()
    url = reverse("kot_OrderChannel_update", args=[instance.pk, ])
    data = {
        "name": "text",
        "close_time": datetime.now(),
        "open_time": datetime.now(),
        "description": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302
