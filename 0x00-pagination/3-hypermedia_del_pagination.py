#!/usr/bin/env python3
"""
    Defines class Server
"""

import csv
from typing import List, Dict


class Server:
    """
        Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
            Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
            Dataset indexed by sorting position, starting at 0.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
            gets the data with the proper index

            Args:
                index (int, optional): _description_. Defaults to None.
                page_size (int, optional): _description_. Defaults to 10.

            Returns:
                Dict: a dictionary containing index, next_index, page_size and
                data.
        """
        if not index:
            index = 0

        assert index >= 0 and index <= len(self.__indexed_dataset)

        changed: int = 0
        data, data_new = self.dataset(), self.__indexed_dataset
        old: int = len(data)
        new: int = len(data_new)

        if old > new and (data[index] != data_new.get(index)):
            diff = old - new
            for i in range(1, diff + 1):
                if data[index + i] == data_new.get(index):
                    changed = i
                    self.__dataset = list(data_new.values())
                    break

        return {
            "index": index,
            "data": list(data_new.values())[index:index + page_size],
            "page_size": page_size,
            "next_index": index + page_size + changed
        }
