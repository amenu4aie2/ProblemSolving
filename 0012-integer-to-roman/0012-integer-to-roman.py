class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numerals = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }


        s=""
        for i in sorted(roman_numerals.keys(),reverse=True):
            if(num>=i):
                s+=roman_numerals[i]*(num//i)
                num=num%i

        return s