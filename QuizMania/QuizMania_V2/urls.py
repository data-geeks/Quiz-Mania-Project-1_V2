from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index,name="Catalog"),
    path('Test_adder',views.add_test,name='Test_Adder'),
    path('admin_portal',views.admin,name='admin_portal'),
    path('student_data',views.student_data,name='student_data'),
    path('close_stats',views.redirect_stats,name='redirect_stats_close')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)