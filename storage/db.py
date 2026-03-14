import sqlite3

def init_db(db_path="vex_scraper.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # crawl_queue table
    # Added worker_id, last_fetched_at, and backoff_until columns
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS crawl_queue (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT UNIQUE NOT NULL,
            status TEXT NOT NULL DEFAULT 'queued' CHECK (status IN ('queued', 'fetching', 'completed', 'failed', 'skipped')),
            depth INTEGER DEFAULT 0,
            retry_count INTEGER DEFAULT 0,
            worker_id VARCHAR(64) DEFAULT NULL,
            last_fetched_at TIMESTAMP,
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

def reset_fetching_status(db_path="vex_scraper.db"):
    """
    Resets all 'fetching' entries to 'queued' on startup.
    Returns the count of rows that were reset.
    TODO: Once we scale to multi-node, we should only reset rows for this worker or stale heartbeats.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("UPDATE crawl_queue SET status = 'queued' WHERE status = 'fetching'")
    reset_count = cursor.rowcount
    conn.commit()
    conn.close()
    return reset_count

if __name__ == "__main__":
    init_db()
