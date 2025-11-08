from database import database_management
import sqlite3

class Category:
    def __init__(self):
        pass

    def viewVolunteerCategory(self):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM category")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []