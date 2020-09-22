import sqlite3
from catalogapp.models import Pet, Photo
from ..connection import Connection

def create_pet(cursor, row):
    _row = sqlite3.Row(cursor, row)

    pet = Pet()
    pet.id = _row["pet_id"]
    pet.name = _row["name"]
    pet.birthday = _row["birthday"]
    pet.favorite_toy = _row["favorite_toy"]

    photo = Photo()
    photo.id = _row["photo_id"]
    photo.caption = _row["caption"]
    photo.description = _row["description"]

    pet.photo = photo

    return pet

def get_pet(pet_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_pet
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            b.id pet_id,
            b.name,
            b.birthday,
            b.favorite_toy,
            b.photo_id,
            li.id photo_id,
            u.caption,
            u.description,
        FROM catalogapp_pet b
        JOIN catalogapp_photo li ON b.photo_id = li.id
        JOIN auth_user u ON u.id = li.user_id
        WHERE b.id = ?
        """, (pet_id,))

        return db_cursor.fetchone()