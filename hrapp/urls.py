from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = 'hrapp'

urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('employees/', employee_list, name='employee_list'),
    path('employees/<int:employee_id>/', employee_details, name='employee'),
    path('employees/employee_form', employee_form, name='employee_form'),
    path('employees/<int:employee_id>/employee_form/',
         employee_edit_form, name='employee_edit_form'),
    path('departments/form', department_form, name='department_form'),
    path('departments/<int:department_id>',
         department_details, name='department'),
    path('departments/', department_list, name='department_list')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
