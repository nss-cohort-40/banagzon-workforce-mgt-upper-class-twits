import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from ..connection import Connection
from hrapp.models import Computer

def computer_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                c.id,
                c.make,
                c.purchase_date,
                c.decommission_date,
                c.manufacturer
            from hrapp_computer c
            """)

            all_computers = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                computer = Computer()
                computer.id = row['id']
                computer.make = row['make']
                computer.purchase_date = row['purchase_date']
                computer.decommission_date = row['decommission_date']
                computer.manufacturer = row['manufacturer']

                all_computers.append(computer)

        template = 'computers/computer_list.html'
        context = {
            'computers': all_computers
        }
        print(all_computers)
        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                INSERT INTO hrapp_computer
                (
                    manufacturer, make, purchase_date
                    )
                VALUES (?, ?, ?)
                """,
                (form_data['manufacturer'], form_data['make'], form_data['purchase_date']))

            return redirect(reverse('hrapp:computer_list'))
