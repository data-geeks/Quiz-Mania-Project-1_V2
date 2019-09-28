from django.urls import path
from . import views

urlpatterns = [
    path("test_page",views.test,name="test_page"),
    path("base_page",views.base,name="base_page"),
]