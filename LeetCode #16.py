"""
Exercice 16 
You are given an integer array nums of length n and an integer target.

Find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 
"""
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        best_sum = nums[0] + nums[1] + nums[2]
        best_diff = abs(best_sum - target)

        for i in range(n - 2):
            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                diff = abs(total - target)

                if diff < best_diff:
                    best_sum = total
                    best_diff = diff

                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total

        return best_sum


# Tests
print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
print(Solution().threeSumClosest([0, 0, 0], 1))
print(Solution().threeSumClosest([1, 1, 1, 0], 100))
print(Solution().threeSumClosest([1,5,10,15,20,35],32))