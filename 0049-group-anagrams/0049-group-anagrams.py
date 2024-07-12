# ; a d fd fa ;
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram={}
        a=[]
        for i in strs:
            x="".join(sorted(i))
            if(x in anagram.keys()):
                y=anagram[x]
                y.append(i)
                anagram[x]=y
            else:
                anagram[x]=[i]
        print(anagram)
        for i,j in anagram.items():
            a.append(j)
        return a
