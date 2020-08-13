import sqlite3
from django.shortcuts import render, reverse, redirect
from hrapp.models import TrainingProgram
from ..connection import Connection


def get_training_program(training_program_id):
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
            WHERE t.id = ?
            """, (training_program_id,))

        return db_cursor.fetchone()


def training_program_details(request, training_program_id):
    if request.method == "GET":
        training_program = get_training_program(training_program_id)
        template = 'training_programs/training_program_details.html'
        
        
        return render(request, template, {"training_program": training_program})

       