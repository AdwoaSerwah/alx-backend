#!/usr/bin/env python3
"""
Defines a Server class to paginate a database of popular baby names.
"""

import csv
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude header row
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page of the dataset (list of rows) based on pagination
        parameters.

        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows corresponding to the page, or
            an empty list if out of range.

        Raises:
            AssertionError: If page or page_size are not positive integers.
        """
        # Validate inputs
        # assert isinstance(page, int) and page > 0, "page must be + integer"
        assert (
            isinstance(page, int) and page > 0
        ), "page must be a positive integer"
        assert (
            isinstance(page_size, int) and page_size > 0
        ), "page_size must be a positive integer"

        # Determine start and end indexes using index_range
        start_index, end_index = index_range(page, page_size)

        # Return the appropriate slice of the dataset
        dataset = self.dataset()
        return dataset[start_index:end_index]
