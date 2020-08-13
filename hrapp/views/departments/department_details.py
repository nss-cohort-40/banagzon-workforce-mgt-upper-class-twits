import sqlite3
from django.shortcuts import render, reverse, redirect
from hrapp.models import Department, Employee
from ..connection import Connection


def create_department(cursor, row):
    _row = sqlite3.Row(cursor, row)

    department = Department()
    department.id = _row["department_id"]
    department.department_name = _row["department_name"]
    department.department_budget = _row["department_budget"]

    department.employees = []

    employee = Employee()
    employee.id = _row["employee_id"]
    employee.first_name = _row["first_name"]
    employee.last_name = _row["last_name"]

    return department


def get_department(department_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_department

        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
                d.id,
                d.department_name,
                d.department_budget,
                e.id employee_id,
                e.department_id,
                e.first_name,
                e.last_name
            FROM hrapp_department d
            JOIN hrapp_employee e ON e.department_id = d.id
        WHERE d.id = ?
        """, (department_id,))

        return db_cursor.fetchone()


def department_details(request, department_id):
    if request.method == "GET":
        department = get_department(department_id)
        template = "departments/department_details.html"

        return render(request, template, {"department": department})
