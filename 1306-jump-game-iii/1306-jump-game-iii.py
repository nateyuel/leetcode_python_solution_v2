class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True
        
        n = len(arr)
        visited = set()
        possible = False
        queue = deque([start])
        queue_set = set([start])
        while queue:
            poped = queue.popleft()
            queue_set.discard(poped)
            visited.add(poped)
            x = poped + arr[poped]
            y = poped - arr[poped]
            if x < n:
                if arr[x] == 0:
                    possible = True
                    break
                elif x not in visited and x not in queue_set:
                    queue.append(x)
                    queue_set.add(x)
                    
            if y >= 0:
                if arr[y] == 0:
                    possible = True
                    break
                elif y not in visited and y not in queue_set:
                    queue.append(y)
                    queue_set.add(y)
        
        return possible 