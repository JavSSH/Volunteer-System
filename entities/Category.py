from database import database_management
import sqlite3

class Category:
    def __init__(self, category_id=None, category_name=None, category_desc=None):
        self.category_id = category_id
        self.category_name = category_name
        self.category_desc = category_desc

    def createVolunteerCategory(self, category_name, category_desc):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("INSERT INTO category (category_name, category_desc) VALUES (?, ?)", 
                       category_name, category_desc)
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
        return [Category(**dict(row)) for row in rows] if rows else []
    
    def updateVolunteerCategory(self, category_id, category_name, category_desc):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("UPDATE category SET category_name = ?, category_desc = ? WHERE category_id = ?", 
                       (category_name, category_desc, category_id,))
        conn.commit()
        conn.close()
        return True

    def deleteVolunteerCategory(self, category_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("DELETE FROM category WHERE category_id = ?", (category_id,))
        conn.commit()
        conn.close()
        return True
    
    def searchVolunteerCategory(self, keyword):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM category WHERE category_name LIKE ? OR category_desc LIKE ?", 
                       ('%' + keyword + '%','%' + keyword + '%'))
        rows = cursor.fetchall()
        conn.close()
        return [Category(**dict(row)) for row in rows] if rows else []
    
    def __str__(self):
        return (f"Category(\n"
            f"  category_id={self.category_id},\n"
            f"  category_name={self.category_name},\n"
            f"  category_desc={self.category_desc},\n"
            f")")