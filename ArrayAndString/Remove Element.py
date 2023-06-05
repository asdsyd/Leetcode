# https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
# Sat 3 June 2023
# Question 2
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] == val:
                nums.remove(val)
                count += 1

        k =


