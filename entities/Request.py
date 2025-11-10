from database import database_management
import sqlite3
import datetime

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
 
    def createRequest(self, user_id, category_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("INSERT INTO request (user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) VALUES (?, ?, false, strftime('%d/%m/%Y', 'now'), 0, 0)", (user_id, category_id))
        conn.commit()
        request_id = cursor.lastrowid
        conn.close()
        return request_id

    def requestViews(self, user_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT category_id, request_status, request_date, request_view_count FROM request WHERE user_id = ? AND request_status = false", (user_id,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []

    def requestShortlist(self, user_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT request_id, request_status, request_date, request_shortlist_count FROM request WHERE user_id = ? AND request_status = false", (user_id,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []
    
    def viewRequests(self, user_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM request WHERE user_id = ?", (user_id,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []
    

    def updateRequest(self, category_id, request_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("UPDATE request SET category_id = ? WHERE request_id = ?", (category_id, request_id))
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
        cursor.execute("""SELECT r.request_id, r.request_date, r.request_view_count, c.category_name, c.category_desc
        FROM request r
        JOIN category c ON r.category_id = c.category_id
        WHERE r.user_id = ?""", (user_id,))
        conn.commit()
        conn.close()
        return True
    
    def requestShortlist(self, user_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT request_id, request_shortlist_count FROM request WHERE user_id = ?", (user_id,))
        conn.commit()
        conn.close()
        return True
    
    def viewCompletedRequests(self, user_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM request WHERE user_id = ? AND request_status = true", (user_id,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []
    
    def filterCompletedRequests(self, user_id, request_date1, request_date2):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM request WHERE user_id = 1 AND request_status = 1 AND date(CASE WHEN request_date LIKE '____-__-__' THEN request_date WHEN request_date LIKE '__/__/____' THEN substr(request_date,7,4) || '-' ||substr(request_date,4,2) || '-' ||substr(request_date,1,2) ELSE NULL END)
        BETWEEN date('?') AND date('?');""", (user_id, request_date1, request_date2))  ## the date params expects in 2025-11-10 format
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []