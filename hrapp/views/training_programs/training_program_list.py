import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from hrapp.models import TrainingProgram
from ..connection import Connection


def training_program_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                t.id,
                t.training_title,
                t.start_date,
                t.end_date,
                t.max_capacity
            from hrapp_trainingprogram t
            """)

            all_training_programs = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                training_program = TrainingProgram()
                training_program.id = row['id']
                training_program.training_title = row['training_title']
                training_program.start_date = row['start_date']
                training_program.end_date = row['end_date']
                training_program.max_capacity = row['max_capacity']
                
                all_training_programs.append(training_program)
            print(all_training_programs)
        template = 'training_programs/training_program_list.html'
        context = {
            'training_programs': all_training_programs
        }
    
        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO hrapp_trainingprogram
            (
                training_title, start_date, end_date, max_capacity
            )
            VALUES (?, ?, ?, ?)
            """,
            (form_data['training_title'], form_data['start_date'], form_data['end_date'], form_data['max_capacity']))

        return redirect(reverse('hrapp:training_program_list'))