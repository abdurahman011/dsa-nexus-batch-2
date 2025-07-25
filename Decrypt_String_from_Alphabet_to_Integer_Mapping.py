class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        decoded_string = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                num_str = s[i-2:i]
                num = int(num_str)
                decoded_string.append(chr(ord('a') + num - 1))
                i -= 3
            else:
                num = int(s[i])
                decoded_string.append(chr(ord('a') + num - 1))
                i -= 1
        
        return "".join(decoded_string[::-1])
