def calculate_fuel(data) -> int:
    total = 0

    for line in data:
        mass = int(line)
        fuel = mass // 3 - 2
        total += fuel

        while ((fuel // 3 - 2) > 0):
            fuel = fuel // 3 - 2
            total += fuel

    return total


def main() -> None:
    with open('input.txt') as file:
        print(calculate_fuel(file))

if __name__ == "__main__":
    main()