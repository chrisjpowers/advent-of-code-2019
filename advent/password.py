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

class Password2:
    def __init__(self, num):
        self.num = num
    
    @property
    def valid(self):
        return self.incrementing() and self.has_double()
    
    def num_list(self):
        return list(map(lambda x: int(x), str(self.num)))

    def incrementing(self):
        nums = [0] + self.num_list()
        for i, num in enumerate(nums):
            if i > 0 and num < nums[i - 1]:
                return False
        return True
    
    def has_double(self):
        nums = [0] + self.num_list() + [0]
        for i in range(1, 6):
            num = nums[i]
            last_num = nums[i - 1]
            next_num = nums[i + 1]
            next_next_num = nums[i + 2]
            if (
                num == next_num and
                num != last_num and
                num != next_next_num
            ):
                return True
        return False