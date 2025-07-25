class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return " "

        prefix = strs[0]

        for i in range(1, len(strs)):
            current_str = strs[i]
            while not current_str.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix
