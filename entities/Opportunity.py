from database import database_management
import sqlite3
import re


class Opportunity:
    def __init__(self, request_id=None, pin_user_id=None, csrrep_user_id=None, category_id=None, request_status=None, request_date=None, request_view_count=None, request_shortlist_count=None):
        self.request_id = request_id
        self.pin_user_id = pin_user_id
        self.csrrep_user_id = csrrep_user_id
        self.category_id = category_id
        self.request_status = request_status
        self.request_date = request_date
        self.request_view_count = request_view_count
        self.request_shortlist_count = request_shortlist_count

    def searchOpportunities(self, keyword):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        clean_keyword = re.sub(r'[^a-zA-Z0-9 ]', '', keyword).strip().lower()
        cursor.execute("""
        SELECT *
        FROM request AS r
        JOIN category AS c
        ON c.category_id = r.category_id
        WHERE LOWER(
            COALESCE(CAST(r.request_id AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.pin_user_id AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.csrrep_user_id AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.category_id AS TEXT), '') || ' ' ||
            COALESCE(c.category_name , '') || ' ' ||
            COALESCE(r.request_status , '') || ' ' ||
            COALESCE(CAST(r.request_date AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.request_view_count AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.request_shortlist_count AS TEXT), '')
        ) LIKE ?
        """,
        (f"%{clean_keyword}%",))
        rows = cursor.fetchall()
        conn.close()
        print([dict(row) for row in rows] if rows else [])
        return [dict(row) for row in rows] if rows else []
        


    def viewOpportunitiesDetails(self):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM request JOIN category ON category.category_id = request.category_id")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []
    
    def addToShortlist(self, request_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("""
        SELECT request_id, pin_user_id
        FROM request
        WHERE request_id = ?
        """, (request_id,))
        row = cursor.fetchone() 
        cursor.execute("""
        INSERT INTO shortlist (
            request_id, user_id
        ) VALUES (?, ?)
        """, (
        row['request_id'],
        row['pin_user_id']
        
        ))
        conn.commit()
        conn.close()
        return True
    
    def searchShortlist(self, csrrep_user_id, keyword):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        clean_keyword = re.sub(r'[^a-zA-Z0-9 ]', '', keyword).strip().lower()
        cursor.execute("""
        SELECT *
        FROM request
        WHERE csr_rep_id = ?
        AND LOWER(
            COALESCE(CAST(request_id AS TEXT), '') || ' ' ||
            COALESCE(CAST(csrrep_user_id AS TEXT), '') || ' ' ||
            COALESCE(CAST(pin_user_id AS TEXT), '') || ' ' ||
            COALESCE(CAST(category_id AS TEXT), '') || ' ' ||
            COALESCE(r.request_status, '') || ' ' ||
            COALESCE(CAST(r.request_date AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.request_view_count AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.request_shortlist_count AS TEXT), '')
        ) LIKE ?
        """,
        (csrrep_user_id, f"%{clean_keyword}%"))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []
    
    def viewShortlist(self, csrrep_user_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM request WHERE csrrep_user_id = ?
        """, (csrrep_user_id,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []
    
    def viewCompletedServices(self, csrrep_user_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM request WHERE csrrep_user_id = ? request_status = true
        """, (csrrep_user_id,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []
    
    def SearchCompletedServices(self,csrrep_user_id,category_id,request_date):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        sql = """
        SELECT
        s.request_id,
        s.pin_user_id,
        s.csrrep_user_id,
        s.category_id,
        s.request_status,
        s.request_date,
        s.request_view_count,
        s.request_shortlist_count,
        c.category_name,
        c.category_desc
        FROM request AS s
        JOIN category AS c
        ON c.category_id = s.category_id
        WHERE 1=1
        """
        params = []
        if csrrep_user_id is not None:
            sql += " AND s.csrrep_user_id = ?"
        params.append(csrrep_user_id)

        if category_id is not None:
            sql += " AND s.category_id = ?"
        params.append(category_id)

        if request_date is not None:
            sql += " AND s.request_date = ?"
        params.append(request_date)

        sql += " ORDER BY s.request_date DESC"
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []
    
    def __str__(self):
        return (f"Opportunity(\n"
                f"  request_id={self.request_id},\n"
                f"  pin_user_id={self.pin_user_id},\n"
                f"  csrrep_user_id={self.csrrep_user_id},\n"
                f"  category_id={self.category_id},\n"
                f"  request_status={self.request_status},\n"
                f"  request_date={self.request_date},\n"
                f"  request_view_count={self.request_view_count},\n"
                f"  request_shortlist_count={self.request_shortlist_count}\n"
                f")")

    
    