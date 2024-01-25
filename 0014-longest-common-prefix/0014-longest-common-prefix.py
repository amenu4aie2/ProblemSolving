class Solution(object):
    

    def longestCommonPrefix(self, strs):
        if(len(strs) >1):
            values = []
            for i in range(1, len(strs)):

                value = 0
                for j in range(0, min(len(strs[0]), len(strs[i]))):
                        print(strs[0][j], strs[i][j])
                        if(strs[0][j] == strs[i][j]):
                            value = value+1
                        else:
                            break
                values.append(value)
            if(len(values) == 0):
                return ""

            else:
                return strs[0][:min(values)]
        else:
            return strs[0]
        