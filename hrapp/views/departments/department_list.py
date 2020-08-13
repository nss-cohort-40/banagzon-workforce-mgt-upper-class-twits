import sqlite3
from django.shortcuts import render
from hrapp.models import Department
from ..connection import Connection
from django.shortcuts import redirect
from django.urls import reverse


def department_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                d.id,
                d.department_name,
                d.department_budget,
                e.department_id
            from hrapp_department d
            left join hrapp_employee e ON e.department_id = d.id
            """)

            dataset = db_cursor.fetchall()

            all_departments = {}

            for row in dataset:
                department = Department()
                department.id = row['id']
                department.department_name = row['department_name']
                department.department_budget = row['department_budget']

                if department.id not in all_departments:
                    print(department.id)
                    all_departments.append(department)

        template = 'departments/department_list.html'
        context = {
            'all_departments': all_departments
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                INSERT INTO hrapp_department
                (
                    department_name, department_budget
                    )
                VALUES (?, ?)
                """,
                              (form_data['department_name'], form_data['department_budget']))

            return redirect(reverse('hrapp:department_list'))
