import random

def compute_backoff(retry_count, base_delay=1.0):
    """
    Computes exponential backoff with jitter.
    Formula: base_delay * (2 ** retry_count) + random(0, base_delay)
    """
    delay = base_delay * (2 ** retry_count)
    jitter = random.uniform(0, base_delay)
    return delay + jitter
