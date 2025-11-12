from database import database_management
import sqlite3

class UserProfile:
    def __init__(self, role_id=None, role_name=None, description=None, status=None):
        self.role_id = role_id
        self.role_name = role_name
        self.description = description
        self.status = status
    
    def createProfile(self, role_id, role_name, description, status):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("INSERT INTO userprofile (role_id, role_name, description, status) VALUES (?, ?, ?, ?)", (role_id, role_name, description, status))
        conn.commit()
        conn.close()
        return True 
    
    def ViewProfile(self):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM userprofile")
        rows = cursor.fetchall()
        conn.close()
        return [UserProfile(**dict(row)) for row in rows] if rows else []
    
    def updateProfile(self, role_id, role_name, description, status):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("UPDATE userprofile SET role_id = ?, role_name = ?, description = ?, status = ? WHERE role_id = ?", (role_id, role_name, description, status,))
        conn.commit()
        conn.close()
        return True
    
    def suspendProfile(self, role_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("UPDATE userprofile SET status = 'false' WHERE role_id = ?", (role_id,))
        conn.commit()
        conn.close()
        return True
    
    def reactivateProfile(self, role_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("UPDATE user SET status = 'true' WHERE role_id = ?", (role_id,))
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
        return [UserProfile(**dict(row)) for row in rows] if rows else []
    
    def __str__(self):
        return (f"UserProfile(\n"
            f"  role_id={self.role_id},\n"
            f"  role_name={self.role_name},\n"
            f"  description={self.description},\n"
            f"  status={self.status},\n"
            f")")
