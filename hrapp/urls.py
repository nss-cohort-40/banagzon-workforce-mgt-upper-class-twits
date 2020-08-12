from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from hrapp import views
from .views import *
from hrapp.models import departments

app_name = 'hrapp'
urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('employees/', employee_list, name='employee_list'),
    path('departments/', department_list, name='department_list'),
    path('employees/<int:employee_id>/', employee_details, name='employee')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
