#!/usr/bin/env python3
"""
Defines a helper function for pagination.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing a start index and an end index
    for a list, based on the given page and page_size.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple (start_index, end_index).
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
