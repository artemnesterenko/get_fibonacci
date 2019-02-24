import logging
from cache_memoize import cache_memoize

logger = logging.getLogger(__name__)


@cache_memoize(300)
def fibonacci(n):
    logger.debug(f"Calculating {n} fibonacci number")
    n = int(n)
    if n < 0:
        raise ValueError("Provide a value greater or equal to 0")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
