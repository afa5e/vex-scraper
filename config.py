# Rate limit defaults
DEFAULT_RATE_LIMIT = 1.0  # seconds between requests
MAX_RETRIES = 3
BASE_DELAY = 1.0          # base delay for exponential backoff (seconds)
POLL_INTERVAL_SECONDS = 5.0 # how long to wait when the queue is empty
DB_PATH = "vex_scraper.db"
USER_AGENT = "VEX-Scraper/0.1"
