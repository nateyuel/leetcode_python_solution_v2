class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g = defaultdict(list)

        for u, v in invocations:
            g[u].append(v)

        bad = [False] * n

        def dfs(u):
            bad[u] = True
            for v in g[u]:
                if not bad[v]:
                    dfs(v)

        dfs(k)

        for u, v in invocations:
            if not bad[u] and bad[v]:
                return list(range(n))

        return [i for i in range(n) if not bad[i]]