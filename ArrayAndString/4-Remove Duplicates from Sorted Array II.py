# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150
# Question 4
# Mon 5 June 2023

class Solution(object):
    def removeDuplicates(self, nums):
        k = 0
        for i in nums:
            if k < 2 or i!=nums[k-2]:
                nums[k] = i
                k += 1

        return k
