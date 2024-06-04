from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=0
        flag=True
        a_dictionary=Counter(s)
        for i,j in a_dictionary.items():
            if(j%2==0):
                count+=j
                a_dictionary[i]=0

            else:
                count+=(j//2)*2
                a_dictionary[i]=1
        a=list(a_dictionary.items())
        a.sort(key=lambda x :x[1],reverse=True)
        count+=a[0][1]
        return count
                
        

        return count