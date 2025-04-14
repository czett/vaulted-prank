import os
import psycopg
from dotenv import load_dotenv

try:
    load_dotenv()
except:
    pass # :) great code, right?

DATABASE_URL = os.getenv("SUPABASE_DB_URL")

def has_downloaded(name: str) -> bool:
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT downloaded FROM users WHERE name = %s", (name,))
            result = cur.fetchone()
            if result:
                return result[0]  # True oder False aus DB
            else:
                raise ValueError(f"Nutzer '{name}' wurde nicht gefunden.")

def get_all_names() -> list:
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT name FROM users")  # Abfrage aller Namen
            result = cur.fetchall()  # Alle Ergebnisse holen
            names = [row[0] for row in result]  # Extrahieren der Namen aus den Ergebnissen
            return names

def get_all_available_names() -> list:
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT name FROM users WHERE downloaded = FALSE")  # Abfrage aller Namen
            result = cur.fetchall()  # Alle Ergebnisse holen
            names = [row[0] for row in result]  # Extrahieren der Namen aus den Ergebnissen
            return names
        
def set_downloaded_true(name: str) -> None:
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE users SET downloaded = %s WHERE name = %s", (True, name))
            conn.commit()  # Änderungen speichern