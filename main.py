class ALPL:
    def __init__(self):
        # self.registers = [None] * 10
        self.registers = {"R" + str(i): None for i in range(10)}
        self.commands = ["LET", "IF", "JUMP", "CALL", "RETURN", "PRINT"]
        self.last_call = None
        self.operations = None
        self.labels = None

    def get_value(self, token):
        try:
            return int(token)
        except ValueError:
            try:
                return self.registers[token]
            except KeyError:
                raise ValueError("...")

    def calculate(self, tokens):
        if len(tokens) not in [1, 3]:
            raise ValueError("incorrect number...")
        if len(tokens) == 1:
            try:
                return self.get_value(tokens[0])
            except KeyError:
                raise ValueError("invalid expression")
        if tokens[1] == "+":
            return self.get_value(tokens[0]) + self.get_value(tokens[2])
        if tokens[1] == "*":
            return self.get_value(tokens[0]) * self.get_value(tokens[2])
        raise ValueError("invalid expression")

    def function_jump(self, tokens):
        try:
            return self.labels[tokens]
        except KeyError:
            raise ValueError("dsadaas")

    def function_return(self):
        return self.last_call + 1

    def function_let(self, tokens):
        if len(tokens) < 2:
            raise ValueError("not enough tokens")
        if tokens[1] != ":=":
            raise ValueError("malformed expression")
        try:
            r_x = tokens[0]
            self.registers[r_x] = self.calculate(tokens[2:])
        except KeyError:
            raise ValueError("...")

    def function_if(self, tokens):
        if len(tokens) != 4:
            raise ValueError("...")
        try:
            r_x = self.registers[tokens[0]]
            r_y = self.registers[tokens[2]]
            label_index = self.labels[tokens[3]]
        except KeyError:
            raise ValueError("dasdas")
        operator = tokens[1]
        if operator not in ["=", "<", ">"]:
            raise ValueError("sdasdasa")
        # todo: include error for the case where the register is empty
        if tokens[1] == "=":
            condition = r_x == r_y
        elif tokens[1] == ">":
            condition = r_x > r_y
        elif tokens[1] == "<":
            condition = r_x < r_y
        return label_index if condition else None

    def execute_operation(self, cur_operation):
        tokens = self.operations[cur_operation].split()
        command = tokens[0]
        if command not in self.commands:
            # todo: enrich error
            raise ValueError("command not supported")
        if command == "LET":
            return self.function_let(tokens[1:])
        elif command == "IF":
            return self.function_if(tokens[1:])
        elif command == "JUMP":
            return self.function_jump(tokens[1])
        elif command == "CALL":
            self.last_call = cur_operation
            return self.function_jump(tokens[1])
        elif command == "RETURN":
            return self.function_return()
        elif command == "PRINT":
            return self.function_print(tokens[1])

    def get_label(self, label):
        if label[-1] != ":":
            raise ValueError()  # maybe to add a specific error
        pure_label = label[:-1]
        if pure_label in self.commands:
            raise ValueError()  # maybe to add a specific error

    def is_label(self, line):
        return line[-1] == ":"

    def split_commands_and_labels(self, script):
        lines = script.splitlines()
        commands = []
        labels = {}
        cur_command_index = 0
        for line in lines:
            if self.is_label(line):
                labels[line[:-1]] = cur_command_index  # maybe plus one? minus one?
            else:
                commands.append(line)  # to replace with an object of the relevant function
                cur_command_index += 1
        return commands, labels

    # todo: change to "public"
    # todo: verify the input is a string
    # todo: verify the input is uppercase
    def execute_script(self, script):
        self.operations, self.labels = self.split_commands_and_labels(script)
        cur_operation = 0
        while cur_operation < len(self.operations):
            next_operation = self.execute_operation(cur_operation)
            if next_operation:
                cur_operation = next_operation
            else:
                cur_operation += 1

    def function_print(self, tokens):
        try:
            print(self.registers[tokens])
        except KeyError:
            raise ValueError("adsadas")


alpl = ALPL()
script1 = """LET R0 := 0
LET R1 := 10
LOOP:
IF R0 = R1 END
LET R0 := R0 + 1
JUMP LOOP
END:"""

script2 = """LET R5 := 2020
CALL PRINTR5
JUMP END
PRINTR5:
PRINT R5
RETURN
END:"""

alpl.execute_script(script2)
