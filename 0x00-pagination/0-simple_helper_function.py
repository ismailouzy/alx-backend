#!/usr/bin/env python3
"""
index range
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate start and end indexes for pagination.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
