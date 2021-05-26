Graph : Abjacent List
Tracker: Set
node : node

import sys
sys.setrecursionlimit(150000000)
def dfs (Graph,Tracker, node):
      Tracker.add(node)
      
      for child in Graph[node]:
          if child not in tracker:
              dfs(Graph,Tracker,child)
  
