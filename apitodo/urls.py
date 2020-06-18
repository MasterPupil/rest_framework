from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverview, name = "api-overview"),
    path("list", views.task_list, name = "api-list"),
    path("create", views.task_create, name = "api-create"),
    path("detail/<str:pk>", views.task_detail, name = "api-detail"),
    path("update/<str:pk>", views.task_update, name = "api-update"),
    path("delete/<str:pk>", views.task_delete, name = "api-delete")
]