class Solution(object):
    def romanToInt(self, s):
        Dictionary = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10,'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        value=0
        for i in range(0,len(s)):
            if i!=len(s)-1:
                if(Dictionary[s[i]]>=Dictionary[s[i+1]]):
                     value+=Dictionary[s[i]]
                elif((s[i]=='I'and (s[i+1]=='V'or'X'))or (s[i]=='X'and (s[i+1]=='L'or'C'))or(s[i]=='C'and (s[i+1]=='D'or'M')) ):
                     value-=Dictionary[s[i]]
                    
                    
            else:
                
                 value+=Dictionary[s[i]]
        return value
            
                
                
                
            