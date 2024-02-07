class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        x = b[0]
        if a == 1:
            return 1
        for i in range(1, len(b)):
            x = (x * 10) + b[i]
        result = 1

        while x > 0:
            if x % 2 == 1:
                result = ((result % 1337) * (a % 1337)) % 1337
            a = ((a % 1337) * (a % 1337)) % 1337
            x //= 2
        return result
