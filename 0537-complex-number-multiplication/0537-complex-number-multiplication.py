class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a,b,c,d= map(int,((num1+num2).replace('+',' ').replace('i'," ")).split())
        return f'{a*c+(-1*d*b)}+{a*d+b*c}i'