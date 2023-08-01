"""
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.



Example 1:

Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
"""


class Solution:

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = collections.defaultdict(set)
        for account in accounts:
            for email in account[1:]:
                graph[account[1]].add(email)
                graph[email].add(account[1])

        visited = set()

        # graph:
        # {'johnsmith@mail.com': {'john_newyork@mail.com', 'johnsmith@mail.com', 'john00@mail.com'},
        # 'john_newyork@mail.com': {'johnsmith@mail.com'},
        # 'john00@mail.com': {'johnsmith@mail.com'},
        # 'mary@mail.com': {'mary@mail.com'},
        # 'johnnybravo@mail.com': {'johnnybravo@mail.com'} }
        def dfs(email: str) -> List[str]:

            if email in visited:
                return []

            visited.add(email)
            for nei in graph[email]:
                dfs(nei)
            self.res.append(email)
            return self.res

        ans = []
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in visited:
                    self.res = []
                    dfs(email)
                    ans.append([name] + sorted(self.res))

        return ans
