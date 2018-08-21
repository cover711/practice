class Solution(object):
    def flipAndInvertImage(self, A):
        B=[]
        for i in A:
            i = [b^1 for b in i]
            B.append(i[::-1])
        #print B
        return B
'''class Solution(object):
    def flipAndInvertImage(self, A):
        B=[]
        C=[]
        D=[]
        f=[0,0,0]
        temp=[]
        #a=0
        for i in A:
            f=[0,0,0]
            a=0
            for b in i:
                if b == 1:
                    f[a] = 0
                else:
                    f[a] = 1
                a=a+1
            D.append(f)
            a=0
        C=D.reverse()
        return D
 '''
