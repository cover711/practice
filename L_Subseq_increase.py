class Solution(object):
    def findLengthOfLCIS(self, nums):
        i=0
        j=1
        nums=[2,4,7,9,2]
        while nums[i]<nums[j]:
            i=i+1
            j=j+1
        print nums[0:j]
        return j
