import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

from menu import models as menu_models
from kod import models as kod_models
from kot import models as kot_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_menu_Category(**kwargs):
    defaults = {}
    defaults["description"] = ""
    defaults["name"] = ""
    defaults.update(**kwargs)
    return menu_models.Category.objects.create(**defaults)
def create_menu_Item(**kwargs):
    defaults = {}
    if "item_category" not in kwargs:
        defaults["item_category"] = create_menu_Category()
    defaults.update(**kwargs)
    return menu_models.Item.objects.create(**defaults)
def create_kod_KOD(**kwargs):
    defaults = {}
    defaults["staff_id"] = ""
    if "kod_nemu_item" not in kwargs:
        defaults["kod_nemu_item"] = create_menu_Item()
    if "kod_status" not in kwargs:
        defaults["kod_status"] = create_kod_Status()
    defaults.update(**kwargs)
    return kod_models.KOD.objects.create(**defaults)
def create_kod_Status(**kwargs):
    defaults = {}
    defaults["status"] = ""
    defaults.update(**kwargs)
    return kod_models.Status.objects.create(**defaults)
def create_kot_KOTMenuItem(**kwargs):
    defaults = {}
    defaults["quantity"] = ""
    if "menu_item" not in kwargs:
        defaults["menu_item"] = create_menu_Item()
    if "kot" not in kwargs:
        defaults["kot"] = create_kot_KOT()
    defaults.update(**kwargs)
    return kot_models.KOTMenuItem.objects.create(**defaults)
def create_kot_KOTStatus(**kwargs):
    defaults = {}
    defaults["status"] = ""
    defaults.update(**kwargs)
    return kot_models.KOTStatus.objects.create(**defaults)
def create_kot_KOT(**kwargs):
    defaults = {}
    defaults["staff_id"] = ""
    defaults["out_time"] = datetime.now()
    defaults["in_time"] = datetime.now()
    if "status" not in kwargs:
        defaults["status"] = create_kot_KOTStatus()
    if "order_channel" not in kwargs:
        defaults["order_channel"] = create_kot_OrderChannel()
    defaults.update(**kwargs)
    return kot_models.KOT.objects.create(**defaults)
def create_kot_OrderChannel(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults["close_time"] = datetime.now()
    defaults["open_time"] = datetime.now()
    defaults["description"] = ""
    defaults.update(**kwargs)
    return kot_models.OrderChannel.objects.create(**defaults)
