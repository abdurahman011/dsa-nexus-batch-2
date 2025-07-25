class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        interpreted_string = []
        i = 0
        n = len(command)
        while i < n:
            if command[i] == 'G':
                interpreted_string.append("G")
                i += 1
            elif command[i:i+2] == "()":
                interpreted_string.append("o")
                i += 2
            elif command[i:i+4] == "(al)":
                interpreted_string.append("al")
                i += 4
        return "".join(interpreted_string)
