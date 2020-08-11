from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from hrapp import views
from .views import *

app_name = 'hrapp'

urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('employees/', employee_list, name='employee_list'),
    path('employees/employee_form', employee_form, name='employee_form'),
    path('employees/<int:employee_id>/', employee_details, name='employee')
]
