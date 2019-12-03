import unittest
import operator

def compute(intcode, noun, verb) -> int:
    done = False
    opcode_loc = 0

    intcode[1] = noun
    intcode[2] = verb

    opcode_rules = {
        1: operator.add,
        2: operator.mul
    }
    
    while not done:
        opcode = intcode[opcode_loc]

        input1_pos = intcode[opcode_loc + 1]
        input2_pos = intcode[opcode_loc + 2]
        output_pos = intcode[opcode_loc + 3]

        input1 = intcode[input1_pos]
        input2 = intcode[input2_pos]

        opcode_func = opcode_rules.get(opcode)
        intcode[output_pos] = opcode_func(input1, input2)
        
        opcode_loc += 4

        if (intcode[opcode_loc] == 99):
            done = True

    return intcode[0]


def get_input() -> tuple:
    with open('input.txt', 'r') as file:
        data = file.readlines()[0]
        data = data.split(',')
        data = tuple(map(lambda x: int(x), data))

        return data;

def main() -> None:
    noun, verb = 0, 0
    data = get_input()

    while True:
        output = compute(list(data), noun, verb)

        if verb >= 99:
            noun += 1
            verb = 0

        if output == 19690720:
            result = {
                'output': output,
                'noun': noun,
                'verb': verb,
                'result': 100 * noun + 44
            }
            print(result)
            break

        verb += 1



if __name__ == "__main__":
    main()