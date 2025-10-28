import database.database_management as db
import sqlite3

class UserAdmin:
    def viewUser(self):
        conn = db.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user ORDER BY user_id ASC")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []