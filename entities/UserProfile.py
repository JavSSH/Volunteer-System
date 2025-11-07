from database import database_management
import sqlite3

class UserProfile:
    def createProfile(self, user_id, role_id, description, status):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("INSERT INTO userprofile (user_id, role_id, role_name, description, status) VALUES (?, ?, ?)", (user_id, role_id, description, status))
        conn.commit()
        conn.close()
        return True 
    
    def getProfile(self, user_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM userprofile WHERE user_id = ?", (user_id,))
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
        cursor.execute("SELECT * FROM userprofile WHERE role_name LIKE ? OR description LIKE ?", ('%' + keyword + '%','%' + keyword + '%'))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []
    
