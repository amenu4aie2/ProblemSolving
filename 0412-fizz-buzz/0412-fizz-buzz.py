class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        out=[]
        for i in range(1,n+1):
            x=""
            if(i%3==0):
                x+="Fizz"
            if (i%5==0):
                x+="Buzz"
            if(len(x)==0):
                x=str(i)
            out.append(x)
        return out