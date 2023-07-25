"""
You are given a All kind of LIST of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

Example 1:
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Example 2:
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
"""


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # tickets: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
        graph = defaultdict(list)

        for d, a in tickets:
            graph[d].append(a)
            graph[d].sort()
        # graph: {'JFK': ['ATL', 'SFO'], 'SFO': ['ATL'], 'ATL': ['JFK', 'SFO']})

        stack = ['JFK']
        result = []

        # result [] stack ['JFK', 'ATL']
        # result [] stack ['JFK', 'ATL', 'JFK']
        # result [] stack ['JFK', 'ATL', 'JFK', 'SFO']
        # result [] stack ['JFK', 'ATL', 'JFK', 'SFO', 'ATL']
        # result [] stack ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']
        # result ['SFO'] stack ['JFK', 'ATL', 'JFK', 'SFO', 'ATL']
        # result ['SFO', 'ATL'] stack ['JFK', 'ATL', 'JFK', 'SFO']
        # result ['SFO', 'ATL', 'SFO'] stack ['JFK', 'ATL', 'JFK']
        # result ['SFO', 'ATL', 'SFO', 'JFK'] stack ['JFK', 'ATL']
        # result ['SFO', 'ATL', 'SFO', 'JFK', 'ATL'] stack ['JFK']
        # result ['SFO', 'ATL', 'SFO', 'JFK', 'ATL', 'JFK'] stack []
        while stack:
            if not graph[stack[-1]]:
                result.append(stack.pop())
            else:
                stack.append(graph[stack[-1]].pop(0))

        return result[::-1]