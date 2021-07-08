'''
Problem Statement
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count1 = 0
        maxConsecutive1 = 0
        
        count = len(nums)
        for i in range(0, count, 1):
            # print(f"nums[i-1] = {nums[i-1]}")
            # print(f"nums[i] = {nums[i]}")
            # print(f"count1 = {count1}")
            # print(f"maxConsecutive1 = {maxConsecutive1}")
                
            if nums[i] == 1:
                count1 = count1 + 1
                # print(f'count1 +1 => {count1}')
                
                if count1 > maxConsecutive1:
                    maxConsecutive1 = maxConsecutive1 + 1
                    # print(f'maxConsecutive1 + 1=> {maxConsecutive1}')
                    
            if nums[i] == 0:
                count1 = 0
                # print(f'count1 reset => {count1}')
                
            
            # print("")
        
        
        # print(maxConsecutive)
        return maxConsecutive1