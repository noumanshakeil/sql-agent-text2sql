import sqlite3
from pathlib import Path

def ensure_db(path: Path = Path("data/demo.db")) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(path)
    con.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price REAL)")
    cur = con.execute("SELECT COUNT(*) FROM products")
    if cur.fetchone()[0] == 0:
        con.executemany(
            "INSERT INTO products(name, price) VALUES (?, ?)",
            [("Laptop", 999), ("Mouse", 25), ("Keyboard", 70)],
        )
        con.commit()
    con.close()
    return path

def run_select(sql: str, path: Path = Path("data/demo.db")):
    if not sql.strip().lower().startswith("select"):
        raise ValueError("Only SELECT allowed")
    con = sqlite3.connect(path)
    rows = con.execute(sql).fetchall()
    con.close()
    return rows
