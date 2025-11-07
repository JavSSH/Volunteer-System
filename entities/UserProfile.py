from database import database_management
import sqlite3

class UserProfile:
    def createProfile(self, role_id, role_name, description, status):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("INSERT INTO userprofile (role_id, role_name, description, status) VALUES (?, ?, ?, ?)", (role_id, role_name, description, status))
        conn.commit()
        conn.close()
        return True 
    
    def viewProfile(self):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM userprofile")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []
    
    def updateProfile(self, user_id, role_id, description, status):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("UPDATE userprofile SET user_id = ?, role_id = ?, description = ?, status = ? WHERE profile_id = ?", (user_id, role_id, description, status,))
        conn.commit()
        conn.close()
        return True
    
    def searchProfile(self, keyword):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM userprofile WHERE description LIKE ?", ('%' + keyword + '%',))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []
    
