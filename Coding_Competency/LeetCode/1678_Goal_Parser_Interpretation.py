class Solution:
    def interpret(self, command):
        return command.replace('()', 'o').replace('(', '').replace(')', '')

print(Solution().interpret("(al)G(al)()()G"))