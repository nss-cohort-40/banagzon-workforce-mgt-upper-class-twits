import sqlite3
from django.shortcuts import render
from hrapp.models import TrainingProgram
from .training_program_details import get_training_program
from ..connection import Connection


def training_form(request):
    if request.method == 'GET':
        template = 'training_programs/training_program_form.html'

        return render(request, template)


def training_edit_form(request, training_program_id):

    if request.method == "GET":
        training_program = get_training_program(training_program_id)

        template = 'training_programs/training_program_form.html'

        return render(request, template, {'training_program': training_program})
