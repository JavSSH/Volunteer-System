from database import database_management
import sqlite3

class Category:
    def __init__(self):
        pass

    def createVolunteerCategory(self, category_name, category_desc):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("INSERT INTO category (category_name, category_desc, category_status) VALUES (?, ?, ?)", 
                       category_name, category_desc, True)
        conn.commit()
        conn.close()
        return True
    
    def viewVolunteerCategory(self):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM category")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []
    
    def updateVolunteerCategory(self, category_id, category_name, category_desc, category_status):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("UPDATE category SET category_name = ?, category_desc = ?, category_status = ? WHERE category_id = ?", (category_name, category_desc, category_status, category_id,))
        conn.commit()
        conn.close()
        return True

    def deleteVolunteerCategory(self, category_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("DELETE FROM category WHERE category_id = ?", category_id)
        conn.commit()
        conn.close()
        return True
    
    def searchVolunteerCategory(self, keyword):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM category WHERE category_name LIKE ? OR category_desc LIKE ?", ('%' + keyword + '%','%' + keyword + '%'))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []