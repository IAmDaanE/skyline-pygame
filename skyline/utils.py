def round_to_num_digits(value, max_digits):
    integer_digits = len(str(abs(int(value))))
    decimal_places = max_digits - integer_digits
    if decimal_places <= 0:
        return int(value)
    return round(value, decimal_places)