def ring(number_of_knocks):
    is_divisible_by_3 = number_of_knocks % 3 == 0
    is_divisible_by_5 = number_of_knocks % 5 == 0
    is_divisible_by_7 = number_of_knocks % 7 == 0

    result = ''

    if is_divisible_by_3:
        result += 'Ding'

    if is_divisible_by_5:
        result += 'Dang'

    if is_divisible_by_7:
        result += 'Dong'

    if result == '':
        result = str(number_of_knocks)

    return result
