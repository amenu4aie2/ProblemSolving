class Solution:
    def __init__(self):
        self.dict={1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M",4:"IV",9:"IX",40:"XL",90:"XC",400:"CD",900:"CM",1000:"M"}
        self.arr=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    def intToRoman(self, num: int,i=0) -> str:
        
        if(num==0):
            return ""
        elif(num>=1000):
            a=""
            for i in range((num//1000)):
                a+="M"
            return a+self.intToRoman(num%1000)
        else:
            a=""
            while i<=11:

                if(num<=self.arr[i] and num>=self.arr[i+1]):
                    
                    for k in range((num//self.arr[i+1])):
                        a+=self.dict[self.arr[i+1]]
                    num=(num%self.arr[i+1])
                    break
                i+=1

            return a+self.intToRoman(num,i)