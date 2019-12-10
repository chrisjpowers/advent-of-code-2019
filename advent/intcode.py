class Intcode:
    def __init__(self, memory, pointer=0, done=False):
        self.pointer = pointer
        self.memory = memory
        self.done = done
    
    def replace(self, pointer, value):
        memory = self.memory.copy()
        memory[pointer] = value
        return Intcode(memory, pointer=self.pointer, done=self.done)

    def compute(self):
        intcode = self
        while intcode.done == False:
            intcode = intcode.run()
        return intcode

    def run(self):
        memory = self.memory.copy()
        command_code = self.memory[self.pointer]
        next_pointer = self.pointer + self.instruction_length
        if command_code == 1:
            memory[self.target_address] = self.parameter_1 + self.parameter_2
            return Intcode(memory, pointer=next_pointer)
        elif command_code == 2:
            memory[self.target_address] = self.parameter_1 * self.parameter_2
            return Intcode(memory, pointer=next_pointer)
        elif command_code == 99:
            return Intcode(memory, pointer=next_pointer, done=True)

    @property
    def instruction_length(self):
        return 4

    @property
    def parameter_1(self):
        return self.value_represented_by_address(self.pointer + 1)
    
    @property
    def parameter_2(self):
        return self.value_represented_by_address(self.pointer + 2)
    
    @property
    def target_address(self):
        return self.value_at_address(self.pointer + 3)
    
    def value_represented_by_address(self, address):
        return self.memory[self.value_at_address(address)]

    def value_at_address(self, address):
        return self.memory[address]
        
    def __eq__(self, other):
        return (
            self.memory == other.memory and
            self.pointer == other.pointer and
            self.done == other.done
        )

    def __repr__(self):
        memory = ','.join([str(c) for c in self.memory])
        return f"<Intcode done={self.done} pointer={self.pointer} memory={memory}>"