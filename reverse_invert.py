class Solution(object):
    def flipAndInvertImage(self, A):
        B=[]
        for i in A:
            i = [b^1 for b in i]
            B.append(i[::-1])
        #print B
        return B
