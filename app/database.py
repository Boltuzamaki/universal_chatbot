import sqlite3

DATABASE = "users.db"

def create_tables():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()

def add_user(username: str, email: str, password: str):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute(
        """
        INSERT INTO users (username, email, password)
        VALUES (?, ?, ?)
        """,
        (username, email, password)
    )
    conn.commit()
    conn.close()

def get_user(username: str, password: str):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute(
        """
        SELECT * FROM users WHERE username = ? AND password = ?
        """,
        (username, password)
    )
    user = c.fetchone()
    conn.close()
    return user