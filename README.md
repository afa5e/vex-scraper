# vex-scraper

A specialized scraper for VEX Knowledge Base and official documentation.

## Scope
- Scrape VEX KB and official docs.
- Structured SQLite storage.
- CLI query interface.
- Phase 1: No forums.

## Data Schema
- `crawl_queue`: Tracks URLs and their crawl state.
- `documents`: Stores scraped content.
