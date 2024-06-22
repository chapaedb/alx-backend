#!/usr/bin/env python3
""" This module includes a helper function for pagination"""

def index_range(page: int, page_size: int)-> tuple:
    """This is gonna return a tuple"""

    start = (page-1) * page_size
    end = start + page_size
    return ( start, end)

