import sqlite3
from django.shortcuts import render, reverse, redirect
from hrapp.models import Computer
from hrapp.models import Employee
from ..connection import Connection


def get_computer(computer_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row

        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
                c.id,
                c.make,
                c.purchase_date,
                c.decommission_date,
                c.manufacturer
            from hrapp_computer c
        WHERE c.id = ?
        """, (computer_id,))

        return db_cursor.fetchone()


def computer_details(request, computer_id):
    if request.method == "GET":
        computer = get_computer(computer_id)
        template = "computers/computer_details.html"

        return render(request, template, {"computer": computer})

    if request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for deleting a book
        #
        # Note: You can use parenthesis to break up complex
        #       `if` statements for higher readability
    if (
        "actual_method" in form_data
        and form_data["actual_method"] == "DELETE"
    ):
        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            DELETE FROM hrapp_computer
            WHERE id = ?
            """, (computer_id,))
        return redirect(reverse('hrapp:computer_list'))
