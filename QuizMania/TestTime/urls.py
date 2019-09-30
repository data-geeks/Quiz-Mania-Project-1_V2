from django.urls import path
from . import views

urlpatterns = [
    path('test_page',views.test,name='test_page'),  # this is link to main test page changes dynamically
    path('base',views.initial,name='base')  # this is link to index test page stays static
]