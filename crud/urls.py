from django.urls import path
from .views import CRUDView

urlpatterns = [
    path('crud/', CRUDView, name="crud_view"),
]
