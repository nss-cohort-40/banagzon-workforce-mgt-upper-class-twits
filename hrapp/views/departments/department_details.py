import sqlite3
from django.shortcuts import render, reverse, redirect
from hrapp.models import Department, Employee
from .department_list import create_departmant
from ..connection import Connection


def get_department(department_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_departmant

        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
                d.id,
                d.department_name,
                d.department_budget,
                e.id employee_id,
                e.department_id,
                e.first_name,
                e.last_name,
                e.start_date,
                e.is_supervisor
            FROM hrapp_department d
            JOIN hrapp_employee e ON e.department_id = d.id
        WHERE d.id = ?
        """, (department_id,))

        return db_cursor.fetchone()


def department_details(request, department_id):
    if request.method == "GET":
        department = get_department(department_id)
        template = "departments/department_details.html"

        return render(request, template, {"department": department.values()})
