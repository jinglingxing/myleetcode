class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        diff = []
        if len(s) != len(goal):
            return False

        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)

        if s == goal and len(s) != len(set(s)):
            return True

        return (len(diff) == 2 and s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]])
