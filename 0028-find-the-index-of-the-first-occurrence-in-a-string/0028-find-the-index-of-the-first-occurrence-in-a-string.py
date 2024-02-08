class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0

        if len(needle) == 1 and len(haystack) == 1 and needle == haystack:
            return 0
        while i != len(haystack) - len(needle) + 1 and (len(haystack) >= len(needle)):
            t = i
            flag = True
            for j in range(len(needle)):
                if needle[j] == haystack[t]:
                    t += 1
                else:
                    flag = False
                    break
            if flag == True:
                print(i)
                return i
            else:
                i += 1
        print(-1)
        return -1
