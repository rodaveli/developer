import sqlite3

def create_connection():
    conn = sqlite3.connect("campaign_crm.db")
    return conn

def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS voters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        date_of_birth TEXT,
        phone_number TEXT,
        email TEXT,
        instagram TEXT,
        facebook TEXT,
        key_issues TEXT,
        data_consent TEXT,
        address TEXT,
        location TEXT,
        referral INTEGER,
        vote_intent TEXT,
        FOREIGN KEY (referral) REFERENCES voters (id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        associated_voter INTEGER,
        date_submitted TEXT,
        location TEXT,
        status TEXT,
        FOREIGN KEY (associated_voter) REFERENCES voters (id)
    )
    """)

    conn.commit()

def init_db():
    conn = create_connection()
    create_tables(conn)
    conn.close()

if __name__ == "__main__":
    init_db()