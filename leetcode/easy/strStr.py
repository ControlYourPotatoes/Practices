

def strStr(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

# Test cases
print(strStr('hello', 'll'))  # 2