from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="Catalog"),
    path('Test_adder',views.add_test,name='Test_Adder'),
    path('admin_portal',views.admin,name='admin_portal'),
    path('student_data',views.student_data,name='student_data')
]