from database import database_management
import sqlite3


class Request:
    def __init__(self, request_id=None, user_id=None, category_id=None, request_status=None, request_date=None, request_view_count=None, request_shortlist_count=None, category_name=None, category_desc=None):
        self.request_id = request_id
        self.user_id = user_id
        self.category_id = category_id
        self.request_status = request_status
        self.request_date = request_date
        self.request_view_count = request_view_count
        self.request_shortlist_count = request_shortlist_count
        self.category_name = category_name
        self.category_desc = category_desc
 
    def createRequest(self, user_id, category_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("INSERT INTO request (user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) VALUES (?, ?, false, strftime('%d/%m/%Y', 'now'), 0, 0)", (user_id, category_id))
        conn.commit()
        request_id = cursor.lastrowid
        conn.close()
        return True
    
    def viewRequests(self, user_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("""
            SELECT r.*, c.category_name, c.category_desc
            FROM request r
            LEFT JOIN category c ON r.category_id = c.category_id
            WHERE r.user_id = ? AND r.request_status = 0
        """, (user_id,))
        rows = cursor.fetchall()
        conn.close()
        return [Request(**dict(row)) for row in rows] if rows else []

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
        return [Request(**dict(row)) for row in rows] if rows else []
    
    def filterCompletedRequests(self, user_id, category_id, request_date1, request_date2):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM request WHERE user_id = ? AND category_id = ? AND request_status = 1 AND date(CASE WHEN request_date LIKE '____-__-__' THEN request_date WHEN request_date LIKE '__/__/____' THEN substr(request_date,7,4) || '-' ||substr(request_date,4,2) || '-' ||substr(request_date,1,2) ELSE NULL END)
        BETWEEN date('?') AND date('?');""", (user_id, category_id, request_date1, request_date2))  ## the date params expects in 2025-11-10 format
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []
    
    def __str__(self):
        return (f"Request(\n"
                f"  request_id={self.user_id},\n"
                f"  user_id={self.user_id},\n"
                f"  category_id={self.category_id},\n"
                f"  request_status={self.request_status},\n"
                f"  request_date={self.request_date},\n"
                f"  request_view_count={self.request_view_count},\n"
                f"  request_shortlist_count={self.request_shortlist_count}\n"
                f")")
