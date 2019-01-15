class Solution:
    def containsDuplicate(self, nums):
        len_nums = len(nums)
        temp_set = set()
        for i in range(0, len_nums, 1):
            temp_set.add(nums[i])
            if len(temp_set) < i+1:
                return True
        return False
