import sqlite3
from django.shortcuts import render, reverse, redirect
from hrapp.models import Department
from ..connection import Connection

def get_department(department_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row

        db_cursor = conn.cursor()
        db_cursor.execute("""
        select
                d.id,
                d.department_name,
                d.department_budget
            from hrapp_department d
        WHERE d.id = ?
        """, (department_id,))

        return db_cursor.fetchone()


def department_details(request, department_id):
    if request.method == "GET":
        department = get_department(department_id)
        template = "departments/department_details.html"

        return render(request, template, {"department": department})
