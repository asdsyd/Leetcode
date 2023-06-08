#https://leetcode.com/problems/majority-element?envType=study-plan-v2&envId=top-interview-150
#Question 5
#Tue 6 June 2023
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        array of size n
        return the majority element

        The majority element is defined as 
        element that appears more than n/2 times that is more than half the times the size of array
        Also it is assumed that the majority element exists in the array (So we dont have to put a check condition)
        '''
        ele = None
        count = 0 
        for i in nums:
            if count == 0:
                ele = i
                count += 1
            elif i == ele:
                count += 1
            else:
                count -= 1
        return ele