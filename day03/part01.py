DIR_MAPPING = {
    'R': (1, 0),
    'L': (-1, 0),
    'D': (0, 1),
    'U': (0, -1),
}


def compute(data):
    dirs = []

    for each in data:
        pos, bla = each[0], each[1:]
        direction = DIR_MAPPING[pos]

        for i in range(0, int(bla)):
            dirs.append(direction)

        print(pos, bla)

def get_input() -> tuple:
    with open('input.txt', 'r') as file:
        data = file.readlines()[0]
        data = data.split(',')
        data = tuple(map(lambda x: int(x), data))

        return data;

def main() -> None:
    data = "R75,D30,R83,U83,L12,D49,R71,U7,L7U62,R66,U55,R34,D71,R55,D58,R83"
    data = data.split(',')
    print(compute(data))

if __name__ == "__main__":
    main()