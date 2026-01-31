import sqlite3
from pathlib import Path

db_path = Path(__file__).parent / "schema.db"

# Create database file if it doesn't exist
if not db_path.exists():
    conn = sqlite3.connect(db_path)
    conn.close()
    print(f"Database created at {db_path}")