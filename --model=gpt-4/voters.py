```python
import sqlite3
from database import Database

class Voters:
    def __init__(self):
        self.db = Database()

    def create_voter(self, full_name, date_of_birth, phone_number, email, instagram, facebook, key_issues, data_consent, address, location, referral, vote_intent):
        query = "INSERT INTO voters (full_name, date_of_birth, phone_number, email, instagram, facebook, key_issues, data_consent, address, location, referral, vote_intent) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        self.db.execute_query(query, (full_name, date_of_birth, phone_number, email, instagram, facebook, key_issues, data_consent, address, location, referral, vote_intent))

    def read_voter(self, voter_id):
        query = "SELECT * FROM voters WHERE id = ?"
        return self.db.fetch_one(query, (voter_id,))

    def update_voter(self, voter_id, full_name, date_of_birth, phone_number, email, instagram, facebook, key_issues, data_consent, address, location, referral, vote_intent):
        query = "UPDATE voters SET full_name = ?, date_of_birth = ?, phone_number = ?, email = ?, instagram = ?, facebook = ?, key_issues = ?, data_consent = ?, address = ?, location = ?, referral = ?, vote_intent = ? WHERE id = ?"
        self.db.execute_query(query, (full_name, date_of_birth, phone_number, email, instagram, facebook, key_issues, data_consent, address, location, referral, vote_intent, voter_id))

    def delete_voter(self, voter_id):
        query = "DELETE FROM voters WHERE id = ?"
        self.db.execute_query(query, (voter_id,))

    def get_all_voters(self):
        query = "SELECT * FROM voters"
        return self.db.fetch_all(query)

    def filter_voters(self, filter_params):
        query = "SELECT * FROM voters WHERE "
        conditions = []
        values = []

        for key, value in filter_params.items():
            conditions.append(f"{key} = ?")
            values.append(value)

        query += " AND ".join(conditions)
        return self.db.fetch_all(query, tuple(values))

    def sort_voters(self, sort_by, order="ASC"):
        query = f"SELECT * FROM voters ORDER BY {sort_by} {order}"
        return self.db.fetch_all(query)
```