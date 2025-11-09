from database import database_management
import sqlite3

class Request:
    def __init__(self, request_id, pin_id, category_id, opportunity_id, request_status, request_date, request_view_count, request_shortlist_count):
        self.request_id = request_id
        self.pin_id = pin_id
        self.category_id = category_id
        self.opportunity_id = opportunity_id
        self.request_status = request_status
        self.request_date = request_date
        self.request_view_count = request_view_count
        self.request_shortlist_count = request_shortlist_count

    def createRequest(self, pin_id, category_id):
        self.pin_id = pin_id
        self.category_id = category_id
        return self.pin_id, self.category_id


    def requestViews(self, request_id):
        self.request_id = request_id
        if request_id:
            self.request_view_count = 100
        return self.request_view_count

    
    def requestShortlist(self, request_id, opportunity_id):
        self.request_id = request_id
        self.opportunity_id = opportunity_id
        if request_id and opportunity_id:
            self.request_shortlist_count = 10
        return self.request_shortlist_count
    
    def viewRequests(self, user_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM request WHERE pin_id = ?", (user_id,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []
    

    def updateRequest(self, request_id, request_detail):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("UPDATE request SET request_detail = ? WHERE request_id = ?", (request_detail, request_id))
        conn.commit()
        conn.close()
        return True
    
    def deleteRequest(self, request_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("DELETE FROM request WHERE request_id = ?", (request_id,))
        conn.commit()
        conn.close()
        return True
    
    def requestViews(self, user_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT request_view_count,request_description FROM request WHERE pin_id = ?", (user_id,))
        conn.commit()
        conn.close()
        return True
    
    def requestShortlist(self, user_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM request WHERE pin_id = ?", (user_id,))
        conn.commit()
        conn.close()
        return True
    
    def viewCompletedRequests(self, user_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM request WHERE user_id = ? AND request_status = 1", (user_id,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []
    
    def filterCompletedRequests(self, user_id, category_id, request_date):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM request WHERE user_id = ? AND request_status = 1 AND request_date BETWEEN ? AND ?", (user_id, category_id,request_date))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []