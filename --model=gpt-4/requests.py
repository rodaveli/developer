import sqlite3
from database import Database

class VoterRequest:
    def __init__(self, request_id, name, description, associated_voter, date_submitted, location, status):
        self.request_id = request_id
        self.name = name
        self.description = description
        self.associated_voter = associated_voter
        self.date_submitted = date_submitted
        self.location = location
        self.status = status

class Requests:
    def __init__(self, db_name):
        self.db = Database(db_name)

    def create_request_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS requests (
            request_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            associated_voter INTEGER,
            date_submitted TEXT,
            location TEXT,
            status TEXT,
            FOREIGN KEY (associated_voter) REFERENCES voters (voter_id)
        )
        '''
        self.db.execute_query(query)

    def add_request(self, request):
        query = '''
        INSERT INTO requests (name, description, associated_voter, date_submitted, location, status)
        VALUES (?, ?, ?, ?, ?, ?)
        '''
        data = (request.name, request.description, request.associated_voter, request.date_submitted, request.location, request.status)
        self.db.execute_query(query, data)

    def update_request(self, request):
        query = '''
        UPDATE requests
        SET name = ?, description = ?, associated_voter = ?, date_submitted = ?, location = ?, status = ?
        WHERE request_id = ?
        '''
        data = (request.name, request.description, request.associated_voter, request.date_submitted, request.location, request.status, request.request_id)
        self.db.execute_query(query, data)

    def delete_request(self, request_id):
        query = '''
        DELETE FROM requests
        WHERE request_id = ?
        '''
        data = (request_id,)
        self.db.execute_query(query, data)

    def get_request_by_id(self, request_id):
        query = '''
        SELECT * FROM requests
        WHERE request_id = ?
        '''
        data = (request_id,)
        result = self.db.execute_query(query, data, fetch_one=True)
        if result:
            return VoterRequest(*result)
        return None

    def get_all_requests(self):
        query = '''
        SELECT * FROM requests
        '''
        results = self.db.execute_query(query, fetch_all=True)
        return [VoterRequest(*result) for result in results]

    def get_requests_by_status(self, status):
        query = '''
        SELECT * FROM requests
        WHERE status = ?
        '''
        data = (status,)
        results = self.db.execute_query(query, data, fetch_all=True)
        return [VoterRequest(*result) for result in results]