#!/usr/bin/env python3
"""
    a function named index_range that takes two integer arguments
    page and page_size.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        The function should return a tuple of size two containing a start
        index and an end index corresponding to the range of indexes to
        return in a list for those particular pagination parameters.

        Args:
            page (int): the page_number
            page_size (int): number of items to display per page.

        Returns:
            Tuple[int, int]: a tuple of the start_index and end_index
    """

    start_index: int = (page - 1) * page_size
    end_index: int = start_index + page_size
    return start_index, end_index
