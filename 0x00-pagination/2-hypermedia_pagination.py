#!/usr/bin/env python3
"""
    Defines a class named Server and a function name index_range
"""
import csv
from typing import List, Tuple, Dict, Any, Union as U


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
            Document cache

        Returns:
            List[List]: the document returned.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            get the specified page with the documents

        Args:
            page (int, optional): the page number to display. Defaults to 1.
            page_size (int, optional): the size of document. Defaults to 10.

        Returns:
            List[List]: the document
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        data: List[List] = self.dataset()
        data_len: int = len(data)

        if page > data_len or page_size > data_len:
            return []

        start, end = index_range(page, page_size)
        return data[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        a get_hyper method that takes the same arguments (and defaults) as
        get_page and returns a dictionary containing the following
        key-value pairs:
        * page_size: the length of the returned dataset page
        * page: the current page number
        * data: the dataset page (equivalent to return from previous task)
        * next_page: number of the next page, None if no next page
        * prev_page: number of the previous page, None if no previous page
        * total_pages: the total number of pages in the dataset as an
        integer.

        Args:
            page (int, optional): the page number to display. Defaults to 1.
            page_size (int, optional): the size of document. Defaults to 10.

        Returns:
            Dict[str, Any]: a dictionary with the above description
        """
        data: List[List] = self.get_page(page, page_size)
        tot_pages: int = (len(self.dataset()) + page_size - 1) // page_size
        """ math.ceil can also be used to get the tot_pages
            math.ceil(len(self.__dataset) / page_size)
        """
        prev_page: U[int, None] = None if (page - 1) < 1 else page - 1
        next_page: U[int, None] = None if (page + 1) > tot_pages else page + 1

        return {"page_size": page_size, "page": page, "data": data,
                "next_page": next_page, "prev_page": prev_page,
                "total_pages": tot_pages}
