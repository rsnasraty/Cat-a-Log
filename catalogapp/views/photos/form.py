import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from catalogapp.models import Photo
# from ..helpers.get_photo import get_photo
from ..connection import Connection

def get_photos():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            
            l.id,
            l.name,
            l.birthday,
            l.favorite_toy
        from catalogapp_photos l
        """)

        return db_cursor.fetchall()

@login_required
def photo_form(request, photo_id):

    if request.method == 'GET':
        photo = get_photos(photo_id)

        template = 'photo/form.html'
        context = {
            'photo': photo,
        }

        return render(request, template, context)
    
@login_required
def photo_edit_form(request, photo_id):

    if request.method == 'GET':
        photo = get_photos(photo_id)
        
        template = 'photos/form.html'
        context = {
            'photo': photo,
        }

        return render(request, template, context)