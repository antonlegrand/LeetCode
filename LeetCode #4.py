"""
Exercice 4 : findMedianSortedArrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.v
"""
import math
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
#Concat, sort , appliquer la méthode souhaitée 
# Liste qui peuvent etre posé de façon séquentiel , nombre pair ou impair 
        list_array = nums1 + nums2
        list_sorted = sorted(list_array)
        if len(list_sorted) % 2 != 0:
            position_median = math.ceil(len(list_sorted)/2)-1
            return list_sorted[position_median]
        else:
            position_midceil = len(list_sorted)//2
            position_before_midceil = len(list_sorted)//2-1
            return (list_sorted[position_before_midceil]+list_sorted[position_midceil ] )/ 2

print(Solution().findMedianSortedArrays([1,2],[3,4]))