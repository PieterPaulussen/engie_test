import time

import numpy as np
from flask import current_app


def filter_and_sort(values: list) -> list:
    """
    Filter and sort a list of integers and floats using numpy for performance.

    The list is filtered to only contain numbers that are divisible by 3.
    The list is then sorted in descending order.

    :param values: The list of integers or floats.
    :type values: list of int or float
    :return: The filtered and sorted list
    :rtype: list of int or float
    """
    current_app.logger.info(f"Filtering and sorting {len(values)} values.")

    # Purely for performance testing and because this is a demo.
    start = time.time()

    arr = np.array(values)
    res = arr[arr % 3.0 == 0]
    res[::-1].sort()

    # Purely for performance testing and because this is a demo.
    current_app.logger.info(
        f"Filtering and sorting took {time.time() - start} seconds."
    )
    return res.tolist()
