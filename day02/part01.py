import unittest
import operator

def compute(intcode) -> int:
    done = False
    opcode_loc = 0

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

    return intcode


class MyTest(unittest.TestCase):

    def test(self):
        self.assertEqual(compute([1,0,0,0,99]), [2,0,0,0,99])
        self.assertEqual(compute([2,3,0,3,99]), [2,3,0,6,99])
        self.assertEqual(compute([2,4,4,5,99,0]), [2,4,4,5,99,9801])
        self.assertEqual(compute(
            [1,1,1,4,99,5,6,0,99]), [30,1,1,4,2,5,6,0,99]
        )


def main() -> None:
    with open('input.txt', 'r') as file:
        data = file.readlines()[0]
        data = data.split(',')
        data = list(map(lambda x: int(x), data))

        data[1] = 12
        data[2] = 2

        print(compute(data))


if __name__ == "__main__":
    unittest.main()