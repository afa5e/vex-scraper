import sqlite3

def init_db(db_path="vex_scraper.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # crawl_queue table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS crawl_queue (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT UNIQUE NOT NULL,
            status TEXT NOT NULL DEFAULT 'queued' CHECK (status IN ('queued', 'fetching', 'completed', 'failed', 'skipped')),
            depth INTEGER DEFAULT 0,
            retry_count INTEGER DEFAULT 0,
            backoff_until TIMESTAMP,
            last_error TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # documents table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT UNIQUE NOT NULL,
            title TEXT,
            content TEXT,
            metadata TEXT,
            scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
