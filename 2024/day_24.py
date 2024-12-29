TEST = False
in_file = "./resources/day_24_test.txt" if TEST else "./resources/day_24.txt"


def file_lines():
    inputs = []
    gates =[]

    with open(in_file) as file:
        input, output = file.read().split("\n\n")
        for line in input.splitlines():
            wire, value = line.split(": ")
            inputs.append((wire ,value))
        for g in output.splitlines():
            x, op, y, _, out = g.split()
            # gates[(x, y, op)] = out
            gates.append(gate(x,y,op,out))
    return inputs, gates

def file_lines_2():

    gates = {}
    with open(in_file) as file:
        _, output = file.read().split("\n\n")

        for g in output.splitlines():
            x, op, y, _, out = g.split()
            gates[(*sorted([x, y]), op)] = out

        return gates



class gate():

    def __init__(self, a, b, operation, out):
        self.operation = operation
        self.registers = sorted([a, b])
        self.output = out
        self.a = None
        self.b = None

    def __repr__(self):
        return f"{self.operation} - {self.registers } - {self.output}"

    def operate(self):
        if self.operation == "AND":
            if self.a == "1" and self.b == "1":
                return self.output, "1"

        if self.operation == "OR":
            if self.a == "1" or self.b == "1":
                return self.output, "1"

        if self.operation == "XOR":
            return self.output, str(int(self.a) ^ int(self.b))

        return self.output, "0"

    def store_register(self, value):
        if self.a:
            self.b = value
            return True

        if not self.a:
            self.a = value
            return False


def question_1():
    """Answer to the first question of the day"""
    answer = 0
    inputs, gates = file_lines()

    process_queue = []

    print(inputs)
    print(gates)
    z_outs = []

    while inputs:
        register, signal = inputs.pop()
        for gate in gates:
            if register in gate.registers:
                if gate.store_register(signal):
                    out_reg, value = gate.operate()
                    inputs.append((out_reg, value))
                    # print((out_reg, value))
                    if out_reg[0] == "z":
                        z_outs.append((out_reg, value))


    answer = ""
    for _,out in sorted(z_outs, reverse=True):
        answer += out
    print(answer)

    answer = int(answer,2)


    return answer


def question_2():
    """Answer to the second question of the day"""
    gates = file_lines_2()

    # half adder to start
    sum_ = gates[("x00", "y00", "XOR")]
    carry = gates[("x00", "y00", "AND")]

    for i in range(1, 44):
        if i < 10:
            index = f"0{i}"
        else:
            index = str(i)

        a = gates.get((f"x{index}", f"y{index}", "XOR"))
        b = gates.get((f"x{index}", f"y{index}", "AND"))
        c = gates.get((*sorted([a, carry]), "AND"))
        sum_ = gates[(*sorted([a, carry]), "XOR")]
        carry = gates.get((*sorted([b, c]), "OR"))
        print(sum_, carry)

        if not a or not b or not c or not carry:
            print(i)

    # from input inspection
    bad_gates = [
        "z09",
        "nnf",
        "nhs",
        "z20",
        "kqh",
        "ddn",
        "z34",
        "wrc"
    ]

    return ",".join(sorted(bad_gates))



if __name__ == '__main__':
    # answer_1 = question_1()
    # print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")

# incorrect wires
# y09 AND x09 -> z09
# kgr XOR fvp -> nnf
# gqh XOR tcv -> nhs
# cdk OR rmn -> z20
# y30 XOR x30 -> kqh
# x30 AND y30 -> ddn
# bmh AND spk -> z34
# spk XOR bmh -> wrc

