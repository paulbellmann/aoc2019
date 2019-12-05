start, end = 264360, 746325


def get_amount_of_passwords(start, end) -> int:
    password_amount = 0
    for password in range(start, end):
        if (is_six_digit_rule(password) and is_in_given_range(start, end, password)
                and is_not_decreasing(password) and has_two_adjacent_same_digits(password)):
            password_amount += 1

    return password_amount

def is_six_digit_rule(password) -> bool:
    return len(str(password)) == 6

def is_in_given_range(start, end, password) -> bool:
    return password >= start and password <= end

def is_not_decreasing(password) -> bool:
    last_digit = 0

    for digit in str(password):
        if int(digit) < last_digit:
            return False
        last_digit = int(digit)

    return True

def has_two_adjacent_same_digits(password) -> bool:
    last_digit = 0

    for digit in str(password):
        if int(digit) == last_digit:
            return True
        last_digit = int(digit)

    return False
 
def main() -> None:
    print(is_six_digit_rule(123456))
    print(is_in_given_range(10, 20, 15))
    print(is_not_decreasing(123))
    print(has_two_adjacent_same_digits(123))

    print(get_amount_of_passwords(start, end))


if __name__ == "__main__":
    main()