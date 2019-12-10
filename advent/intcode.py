class Intcode:
    def __init__(self, codes, index=0, done=False):
        self.index = index
        self.codes = codes
        self.done = done
    
    def replace(self, index, value):
        codes = self.codes.copy()
        codes[index] = value
        return Intcode(codes, index=self.index, done=self.done)

    def compute(self):
        intcode = self
        while intcode.done == False:
            intcode = intcode.run()
        return intcode

    def run(self):
        codes = self.codes.copy()
        command_code = self.codes[self.index]
        if command_code == 1:
            codes[self.target_index] = self.left_operand + self.right_operand
            return Intcode(codes, index=self.index + 4)
        elif command_code == 2:
            codes[self.target_index] = self.left_operand * self.right_operand
            return Intcode(codes, index=self.index + 4)
        elif command_code == 99:
            return Intcode(codes, index=self.index + 4, done=True)

    def add(self):
        if self.codes[self.index] == 1:
            codes = self.codes.copy()
            return codes

    @property
    def left_operand(self):
        left_index = self.codes[self.index + 1]
        return self.codes[left_index]
    
    @property
    def right_operand(self):
        right_index = self.codes[self.index + 2]
        return self.codes[right_index]
    
    @property
    def target_index(self):
        return self.codes[self.index + 3]
        
    def __eq__(self, other):
        return (
            self.codes == other.codes and
            self.index == other.index and
            self.done == other.done
        )

    def __repr__(self):
        codes = ','.join([str(c) for c in self.codes])
        return f"<Intcode done={self.done} index={self.index} codes={codes}>"