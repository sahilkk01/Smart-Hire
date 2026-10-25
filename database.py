
import sqlite3


def create_table():
    connection = sqlite3.connect("smarthire.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analysis_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_url TEXT,
            match_score REAL,
            matched_skills TEXT,
            missing_skills TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def save_analysis(job_url, match_score, matched_skills, missing_skills):
    connection = sqlite3.connect("smarthire.db")

    try:
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO analysis_history
            (job_url, match_score, matched_skills, missing_skills)
            VALUES (?, ?, ?, ?)
        """, (
            job_url,
            match_score,
            ", ".join(matched_skills),
            ", ".join(missing_skills)
        ))

        connection.commit()

    finally:
        connection.close()

def get_history():
    connection = sqlite3.connect("smarthire.db")
    connection.row_factory = sqlite3.Row

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT * FROM analysis_history
            ORDER BY id DESC
        """)

        history = cursor.fetchall()
        return history

    finally:
        connection.close()

def delete_history(history_id):
    connection = sqlite3.connect("smarthire.db")

    try:
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM analysis_history WHERE id = ?",
            (history_id,)
        )

        connection.commit()

    finally:
        connection.close()


def clear_all_history():
    connection = sqlite3.connect("smarthire.db")

    try:
        cursor = connection.cursor()

        cursor.execute("DELETE FROM analysis_history")

        connection.commit()

    finally:
        connection.close()


if __name__ == "__main__":
    create_table()
    print("Database table created successfully!")
