from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("KOD", api.KODViewSet)
router.register("Status", api.StatusViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("kod/KOD/", views.KODListView.as_view(), name="kod_KOD_list"),
    path("kod/KOD/create/", views.KODCreateView.as_view(), name="kod_KOD_create"),
    path("kod/KOD/detail/<int:pk>/", views.KODDetailView.as_view(), name="kod_KOD_detail"),
    path("kod/KOD/update/<int:pk>/", views.KODUpdateView.as_view(), name="kod_KOD_update"),
    path("kod/KOD/delete/<int:pk>/", views.KODDeleteView.as_view(), name="kod_KOD_delete"),
    path("kod/Status/", views.StatusListView.as_view(), name="kod_Status_list"),
    path("kod/Status/create/", views.StatusCreateView.as_view(), name="kod_Status_create"),
    path("kod/Status/detail/<int:pk>/", views.StatusDetailView.as_view(), name="kod_Status_detail"),
    path("kod/Status/update/<int:pk>/", views.StatusUpdateView.as_view(), name="kod_Status_update"),
    path("kod/Status/delete/<int:pk>/", views.StatusDeleteView.as_view(), name="kod_Status_delete"),

)
