from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Category", api.CategoryViewSet)
router.register("Item", api.ItemViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("menu/Category/", views.CategoryListView.as_view(), name="menu_Category_list"),
    path("menu/Category/create/", views.CategoryCreateView.as_view(), name="menu_Category_create"),
    path("menu/Category/detail/<int:pk>/", views.CategoryDetailView.as_view(), name="menu_Category_detail"),
    path("menu/Category/update/<int:pk>/", views.CategoryUpdateView.as_view(), name="menu_Category_update"),
    path("menu/Category/delete/<int:pk>/", views.CategoryDeleteView.as_view(), name="menu_Category_delete"),
    path("menu/Item/", views.ItemListView.as_view(), name="menu_Item_list"),
    path("menu/Item/create/", views.ItemCreateView.as_view(), name="menu_Item_create"),
    path("menu/Item/detail/<int:pk>/", views.ItemDetailView.as_view(), name="menu_Item_detail"),
    path("menu/Item/update/<int:pk>/", views.ItemUpdateView.as_view(), name="menu_Item_update"),
    path("menu/Item/delete/<int:pk>/", views.ItemDeleteView.as_view(), name="menu_Item_delete"),

)
