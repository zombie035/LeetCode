class Solution:
    def numberOfPermutations(self, n, requirements):
        MOD = 10**9 + 7

        req = [-1] * n

        for end, cnt in requirements:
            req[end] = cnt

        if req[0] > 0:
            return 0

        req[0] = 0

        max_inv = max(req)

        dp = [0] * (max_inv + 1)
        dp[0] = 1

        for i in range(1, n):

            new_dp = [0] * (max_inv + 1)

            # Sliding window
            window = 0

            for inv in range(max_inv + 1):

                window += dp[inv]

                if inv - i - 1 >= 0:
                    window -= dp[inv - i - 1]

                window %= MOD

                new_dp[inv] = window

            # If this prefix has a requirement,
            # keep only that inversion count.
            if req[i] != -1:
                required = req[i]

                value = new_dp[required]

                new_dp = [0] * (max_inv + 1)
                new_dp[required] = value

            dp = new_dp

        return dp[req[n - 1]]