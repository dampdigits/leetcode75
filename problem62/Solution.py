class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        # Memoization
        evenCache = [0] * (n+1)
        oddCache = [0] * (n+1)

        # Place a domino
        def domino(N):
            if N == 0: return 1
            if evenCache[N]: return evenCache[N]

            ways = domino(N-1) % MOD
            if N-1 > 0:
                ways += (domino(N-2) % MOD) + ((2 * tromino(N-2)) % MOD)
            
            evenCache[N] = ways % MOD
            return evenCache[N]

        # Place a tromino (previously a tromino was placed)
        def tromino(N):
            if N == 0: return 0
            if oddCache[N]: return oddCache[N]

            ways = (tromino(N-1) % MOD) + (domino(N-1) % MOD)
            
            oddCache[N] = ways % MOD
            return oddCache[N]

        return domino(n) % MOD
