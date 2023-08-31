from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("KOTMenuItem", api.KOTMenuItemViewSet)
router.register("KOTStatus", api.KOTStatusViewSet)
router.register("KOT", api.KOTViewSet)
router.register("OrderChannel", api.OrderChannelViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("kot/KOTMenuItem/", views.KOTMenuItemListView.as_view(), name="kot_KOTMenuItem_list"),
    path("kot/KOTMenuItem/create/", views.KOTMenuItemCreateView.as_view(), name="kot_KOTMenuItem_create"),
    path("kot/KOTMenuItem/detail/<int:pk>/", views.KOTMenuItemDetailView.as_view(), name="kot_KOTMenuItem_detail"),
    path("kot/KOTMenuItem/update/<int:pk>/", views.KOTMenuItemUpdateView.as_view(), name="kot_KOTMenuItem_update"),
    path("kot/KOTMenuItem/delete/<int:pk>/", views.KOTMenuItemDeleteView.as_view(), name="kot_KOTMenuItem_delete"),
    path("kot/KOTStatus/", views.KOTStatusListView.as_view(), name="kot_KOTStatus_list"),
    path("kot/KOTStatus/create/", views.KOTStatusCreateView.as_view(), name="kot_KOTStatus_create"),
    path("kot/KOTStatus/detail/<int:pk>/", views.KOTStatusDetailView.as_view(), name="kot_KOTStatus_detail"),
    path("kot/KOTStatus/update/<int:pk>/", views.KOTStatusUpdateView.as_view(), name="kot_KOTStatus_update"),
    path("kot/KOTStatus/delete/<int:pk>/", views.KOTStatusDeleteView.as_view(), name="kot_KOTStatus_delete"),
    path("kot/KOT/", views.KOTListView.as_view(), name="kot_KOT_list"),
    path("kot/KOT/create/", views.KOTCreateView.as_view(), name="kot_KOT_create"),
    path("kot/KOT/detail/<int:pk>/", views.KOTDetailView.as_view(), name="kot_KOT_detail"),
    path("kot/KOT/update/<int:pk>/", views.KOTUpdateView.as_view(), name="kot_KOT_update"),
    path("kot/KOT/delete/<int:pk>/", views.KOTDeleteView.as_view(), name="kot_KOT_delete"),
    path("kot/OrderChannel/", views.OrderChannelListView.as_view(), name="kot_OrderChannel_list"),
    path("kot/OrderChannel/create/", views.OrderChannelCreateView.as_view(), name="kot_OrderChannel_create"),
    path("kot/OrderChannel/detail/<int:pk>/", views.OrderChannelDetailView.as_view(), name="kot_OrderChannel_detail"),
    path("kot/OrderChannel/update/<int:pk>/", views.OrderChannelUpdateView.as_view(), name="kot_OrderChannel_update"),
    path("kot/OrderChannel/delete/<int:pk>/", views.OrderChannelDeleteView.as_view(), name="kot_OrderChannel_delete"),

)
