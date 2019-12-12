class Password:
    def __init__(self, num):
        self.num = num
    
    @property
    def valid(self):
        return self.incrementing() and self.has_double()

    def incrementing(self):
        nums = [0] + list(map(lambda x: int(x), str(self.num)))
        for i, num in enumerate(nums):
            if i > 0 and num < nums[i - 1]:
                return False
        return True
    
    def has_double(self):
        str_num = str(self.num)
        doubles = ['11', '22', '33', '44', '55', '66', '77', '88', '99']
        for double in doubles:
            if double in str_num:
                return True
        return False


