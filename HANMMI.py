class Solution(object):
    def hammingDistance(self, x, y):
        C=[]
        i=0
        y=101
        while y>0:
            C.append(y%2)
            y=y/2
            i+=1
        print C[::-1]
