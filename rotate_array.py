class Solution(object):
    def rotate(self, nums, k):
        i= 0
        a = len(nums)
        while i < a-k:
            b = nums.pop(0)
            nums.append(b)
            i=i+1
        print nums
