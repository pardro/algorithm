class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = num1 + num2
        a.sort()
        a_len = len(a)
        a_center = int(a_len / 2)

        if (a_len % 2 == 1):
            return a[a_center]
        else:
            return (a[a_center - 1] + a[a_center]) / 2.0