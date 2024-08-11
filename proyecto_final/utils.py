def find_first(data: list[dict], **kwargs) -> dict:
    """
    Find the first dictionary in a list that matches the given key-value pairs.

    Args:
        data (list[dict]): A list of dictionaries to search through.
        **kwargs: Arbitrary keyword arguments representing the key-value pairs to match against 
                  the dictionaries in the `data` list.

    Returns:
        dict: The first dictionary from the `data` list that contains all the specified key-value pairs
              provided in `kwargs`. If no matching dictionary is found, an empty dictionary `{}` is returned.

    Example:
        >>> data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
        >>> find_first(data, name='Bob')
        {'name': 'Bob', 'age': 25}

        >>> find_first(data, name='Charlie')
        {}

    Raises:
        None: The function handles exceptions internally and returns an empty dictionary if no match is found.

    Notes:
        - The search is performed using the `filter` function, which iterates through the `data` list
          and applies a lambda function to each dictionary. The lambda checks if all key-value pairs
          in `kwargs` are present and match in the dictionary.
        - The function attempts to return the first matching dictionary. If no matches are found, an empty
          dictionary is returned.

    """
    ans = filter(
        lambda x: all(
            x.get(key) == value for key, value in kwargs.items()
        ), data
    )
    try:
        ans = list(ans)[0]
    except: 
        return {}
    return ans