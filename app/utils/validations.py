"""Various Validation services."""
def validate_integer(
        arg_name: str,
        arg_value: int,
        min_value: int = None,
        max_value: int = None,
        custom_min_msg: str = None,
        custom_max_msg: str = None
):
    """
    Validates that arg_value is an integer, and optional that it is within the specified range.
    A custom override error message can be provided when the min / max value is exceeded.
    Args:
        arg_name (str): the name of the argument (used in default error messages)
        arg_value (obj): the value being validated
        min_value (int): optional, specifies the minimum value (inclusive)
        max_value (int): optional, specifies the maximum value (inclusive)
        custom_min_msg (str): optional, custom message when value is less
            than a minimum
        custom_max_msg (str): optional, custom message when value is greater
            than a maximum


    Returns:
        None: no exceptions are raised if validation passes

    Raises:
        TypeError: if `arg_value` is not an integer
        ValueError: if `arg_value` does not satisfy the bounds


    """
    if not isinstance(arg_value, int):
        raise TypeError(f"{arg_name} must be an integer")
    if min_value is not None and arg_value < min_value:
        if custom_min_msg is not None:
            raise ValueError(custom_min_msg)
        else:
            raise ValueError(f"{arg_name} must be at least {min_value}")
    if max_value is not None and arg_value > max_value:
        if custom_max_msg is not None:
            raise ValueError(custom_max_msg)
        raise ValueError(f"{arg_name} must be at most {max_value}")

