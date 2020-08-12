import sqlite3
from django import forms
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from hrapp.models import Department
from hrapp.models import Employee
from ..connection import Connection

# class HorizRadioRenderer(forms.RadioSelect.renderer):
#     """ this overrides widget method to put radio buttons horizontally
#         instead of vertically.
#     """
#     def render(self):
#             """Outputs radios"""
#             return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

# class HorizRadioRenderer(forms.RadioSelect.renderer):
#     """ this overrides widget method to put radio buttons horizontally
#         instead of vertically.
#     """
#     def render(self):
#             """Outputs radios"""
#             return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

def get_departments():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            d.id,
            d.department_name,
            d.department_budget
        from hrapp_department d
        """)

        return db_cursor.fetchall()

@login_required
def employee_form(request):
    if request.method == 'GET':
        departments = get_departments()
        template = 'employees/employee_form.html'
        context = {
            'all_departments': departments
        }

        return render(request, template, context)

   
             

        

