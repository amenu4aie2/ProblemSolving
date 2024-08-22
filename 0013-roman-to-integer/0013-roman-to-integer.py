class Solution:
    def romanToInt(self, s: str) -> int:
        diction={"I":1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000}
        sum=0
        for i in range(len(s)-1):
            if(diction[s[i]]<diction[s[i+1]]):
                sum-=diction[s[i]]
            else:
                sum+=diction[s[i]]
        sum+=diction[s[-1]]
        return sum