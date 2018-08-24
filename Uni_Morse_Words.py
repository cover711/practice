class Solution(object):
    def uniqueMorseRepresentations(self, words):
        F=[]
        E=[]
        #another way#
        #morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
        # ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        #words = "abcdefghijklmnopqrstuvwxyz"
        #words = list(words)
        #to = {}
        #for i in range(26):
        #   to[words[i]] = morse[i]
        data = {'a':".-", 'b' :"-...", 'c' :"-.-.", 'd' :"-..", 'e' :".", 'f' : "..-.", 'g':"--.", 'h':"....",'i' : "..",'j' : ".---", 'k' : "-.-",'l':".-..",'m':"--",'n' :"-.",'o' : "---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v' :"...-", 'w':".--", 'x':"-..-",'y':"-.--",'z':"--.."}
        for i in words:
            C=[]
            for a in i:
                for key, value in data.iteritems():
                    if key == a:
                        C.append(value)
            F.append(C)
        for i in F:
            E.append(''.join(i))
        print E    
        print set(E)
        print "we got", len(set(E)) ,"types"
        return 0
