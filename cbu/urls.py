from django.contrib import admin
from django.urls import path, include

from cbu.views import SaveCBUDataView

urlpatterns = [
    path('curve/', SaveCBUDataView.as_view({"get":"list","post":"create"})),
]
