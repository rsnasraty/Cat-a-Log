import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from catalogapp.models import Pet
from ..connection import Connection

def get_pets():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            l.id,
            l.name,
            l.birthday,
            l.favorite_toy
        from catalogapp_pets l
        """)

        return db_cursor.fetchall()

@login_required
def pet_form(request, pet_id):

    if request.method == 'GET':
        pet = get_pets(pet_id)

        template = 'pet/form.html'
        context = {
            'pet': pet,
        }

        return render(request, template, context)