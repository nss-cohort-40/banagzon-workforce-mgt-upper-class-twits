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
                t.max_capacity,
            from hrapp_trainingprogram t
            """)

            all_training_programs = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                training_program = TrainingProgram()
                training_program.id = row['id']
                training_program.first_name = row['training_title']
                training_program.last_name = row['start_date']
                training_program.start_date = row['end_date']
                
                all_training_programs.append(training_program)

        template = 'training_program/training_program_list.html'
        context = {
            'training_programs': all_training_programs
        }
    
        return render(request, template, context)

    
    
    
    
    
    
    
    
    
    
    