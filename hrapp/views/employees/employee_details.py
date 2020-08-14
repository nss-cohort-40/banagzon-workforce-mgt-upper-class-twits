import sqlite3
from django.shortcuts import render, reverse, redirect
from hrapp.models import Employee
from ..connection import Connection


def get_employee(employee_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row

        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            e.id,
            e.first_name,
            e.last_name,
            e.start_date,
            e.is_supervisor,
            e.department_id,
            d.id department_id,
            d.department_name
        FROM hrapp_employee e
        JOIN hrapp_department d ON e.department_id = d.id
        WHERE e.id = ?
        """, (employee_id,))

        return db_cursor.fetchone()


def employee_details(request, employee_id):
    if request.method == "GET":
        employee = get_employee(employee_id)
        template = "employees/employee_details.html"

        return render(request, template, {"employee": employee})

    elif request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for editing a book
        if (
            "actual_method" in form_data and form_data["actual_method"] == "PUT"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE hrapp_employee
                SET first_name = ?,
                    last_name = ?,
                    start_date = ?,
                    is_supervisor = ?,
                    department_id = ?
                WHERE id = ?
                """, (form_data['first_name'], form_data['last_name'], form_data['start_date'],
                      form_data['is_supervisor'], form_data["department_id"], employee_id))

            return redirect(reverse('hrapp:employee', args=[employee_id]))
