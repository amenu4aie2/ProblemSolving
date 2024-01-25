class Solution(object):
    def isValid(self, s):
        aray = []
        if(len(s) > 1):
            for i in range(0, int(len(s))):
                dict = {"[": "]", "(": ')', "{": "}", "}": "",
                        ")": "", "]": ""}

                
                if(s[i] == ')' or s[i] == ']' or s[i] == '}'):

                    if(len(aray) >= 1):

                        if(dict[aray.pop()] == s[i]):

                            pass

                        else:

                            return False
                    else:
                        return False

                else:

                    aray.append(s[i])

            if(len(aray) == 0):
                return True
            else:
                return False

        else:
            return False
