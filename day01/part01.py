import argparse
import pytest

"""
Fuel required to launch a given module is based on its mass. Specifically,
to find the fuel required for a module, take its mass, divide by three,
round down, and subtract 2.

The Fuel Counter-Upper needs to know the total fuel requirement.
To find it, individually calculate the fuel needed for the mass of 
each module (your puzzle input), then add together all the fuel values.
"""
def compute(s: str) -> int:
    total = 0
    for line in s.splitlines():
        total += (int(line) // 3) - 2

    return total


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ('12', 2),
        ('14', 2),
        ('1969', 654),
        ('100756', 33583),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_file')
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    main()