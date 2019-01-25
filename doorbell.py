def ring(number_of_knocks):
    is_divisible_by_3 = number_of_knocks % 3 == 0
    is_divisible_by_5 = number_of_knocks % 5 == 0

    if is_divisible_by_3 and is_divisible_by_5:
        return 'DingDong'

    if is_divisible_by_3:
        return 'Ding'

    if is_divisible_by_5:
        return 'Dong'

    return str(number_of_knocks)
