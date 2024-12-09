def sequential_search(a_list, item):
    """Performs a sequencial search on a list."""
    pos = 0

    while pos < len(a_list):
        if a_list[pos] == item:
            return True
        pos = pos + 1

    return False



