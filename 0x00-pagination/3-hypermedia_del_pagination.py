#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude header row
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a dictionary containing deletion-resilient hypermedia
        pagination details.

        Args:
            index (int): The current start index of the return page.
            page_size (int): The number of items per page.

        Returns:
            Dict: A dictionary with deletion-resilient hypermedia
            pagination details.

        Raises:
            AssertionError: If index is not a valid position in the dataset.
        """
        assert (
            isinstance(index, int)
            and 0 <= index < len(self.indexed_dataset())
        ), "Index out of range"

        data = []
        next_index = index
        current_size = 0
        indexed_data = self.indexed_dataset()

        # Gather data until the page is filled or end of dataset
        while current_size < page_size and next_index < len(indexed_data):
            if next_index in indexed_data:
                data.append(indexed_data[next_index])
                current_size += 1
            next_index += 1

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index,
        }
