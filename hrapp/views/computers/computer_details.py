import sqlite3
from django.shortcuts import render, reverse, redirect
from hrapp.models import Computer
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

    