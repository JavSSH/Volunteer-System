from database import database_management
import sqlite3
import re


class Opportunity:
    def __init__(self, opportunity_id=None, request_id=None, pin_user_id=None, csrrep_user_id=None, opportunity_date=None):
        self.opportunity_id = opportunity_id
        self.request_id = request_id    
        self.pin_user_id = pin_user_id
        self.csrrep_user_id = csrrep_user_id
        self.opportunity_date = opportunity_date

    def searchOpportunities(self, keyword):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        clean_keyword = re.sub(r'[^a-zA-Z0-9 ]', '', keyword).strip().lower()
        # cursor.execute("SELECT * FROM user WHERE first_name LIKE ? OR last_name LIKE ? OR email LIKE ? OR phone LIKE ?", ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%'))
        cursor.execute("""
        SELECT *
        FROM request AS r
        JOIN category AS c
        ON c.category_id = r.category_id
        WHERE LOWER(
            COALESCE(CAST(r.request_id AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.user_id AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.category_id AS TEXT), '') || ' ' ||
            COALESCE(c.category_name, '') || ' ' ||
            COALESCE(r.request_status, '') || ' ' ||
            COALESCE(CAST(r.request_date AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.request_view_count AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.request_shortlist_count AS TEXT), '')
        ) LIKE ?
        """,
        (f"%{clean_keyword}%",)
)
        rows = cursor.fetchall()
        conn.close()
        return [Opportunity(**dict(row)) for row in rows] if rows else []
    
    def viewOpportunitiesDetails(self):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM opportunity")
        rows = cursor.fetchall()
        conn.close()
        return [Opportunity(**dict(row)) for row in rows] if rows else []
    
    def addToShortlist(self, opportunity_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("INSERT INTO shortlist (opportunity_id) VALUES (?)", (opportunity_id))
        conn.commit()
        conn.close()
        return True
    
    def searchShortlist(self, csr_rep_id, keyword):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        clean_keyword = re.sub(r'[^a-zA-Z0-9 ]', '', keyword).strip().lower()
        cursor.execute("""
        SELECT r.*
        FROM shortlist AS s
        JOIN request AS r
        ON s.opportunity_id = r.request_id
        WHERE s.csr_rep_id = ?
        AND LOWER(
            COALESCE(CAST(r.request_id AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.user_id AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.category_id AS TEXT), '') || ' ' ||
            COALESCE(r.request_status, '') || ' ' ||
            COALESCE(CAST(r.request_date AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.request_view_count AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.request_shortlist_count AS TEXT), '')
        ) LIKE ?
        """,
        (csr_rep_id, f"%{clean_keyword}%"))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []
    
    def viewShortlist(self, csr_rep_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("""
        SELECT r.*
        FROM shortlist AS s
        JOIN request AS r
        ON s.opportunity_id = r.request_id
        WHERE s.csr_rep_id = ?
        """, (csr_rep_id,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []
    
    def viewCompletedServices(self, csr_rep_id):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("""
        SELECT r.*
        FROM completed_services AS cs
        JOIN request AS r
        ON cs.opportunity_id = r.request_id
        WHERE cs.csr_rep_id = ?
        """, (csr_rep_id,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []
    
    def SearchCompletedServices(self,csr_rep_id, keyword,date):
        conn = database_management.dbConnection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        clean_keyword = re.sub(r'[^a-zA-Z0-9 ]', '', keyword).strip().lower()
        cursor.execute("""
        SELECT r.*
        FROM completed_services AS cs
        JOIN request AS r
        ON cs.opportunity_id = r.request_id
        WHERE cs.csr_rep_id = ?
        AND LOWER(
            COALESCE(CAST(r.request_id AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.user_id AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.category_id AS TEXT), '') || ' ' ||
            COALESCE(r.request_status, '') || ' ' ||
            COALESCE(CAST(r.request_date AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.request_view_count AS TEXT), '') || ' ' ||
            COALESCE(CAST(r.request_shortlist_count AS TEXT), '')
        ) LIKE ?
        """,
        (csr_rep_id, date, f"%{clean_keyword}%"))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows] if rows else []
    
    def __str__(self):
        return (f"Opportunity(\n"
                f"  opportunity_id={self.opportunity_id},\n"
                f"  request_id={self.request_id},\n"
                f"  pin_user_id={self.pin_user_id},\n"
                f"  csrrep_user_id={self.csrrep_user_id},\n"
                f"  opportunity_date={self.opportunity_date}\n"
                f")")

    
    