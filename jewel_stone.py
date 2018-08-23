class Solution(object):
    def numJewelsInStones(self, J, S):
        #J = "abcCE"
        #S = "aEbbCzzzBa"
        count =0
        for i in J:
            for a in S:
                if i == a:
                    count=count+1
        return count
