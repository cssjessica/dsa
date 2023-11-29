class Solution:
    def numberOfWays(self, corridor: str) -> int:
        # time complexity: O(n)
        # space complexity: O(n)

        # mod = 10**9 + 7

        # def dfs(i, seats):
        #     if i == len(corridor):
        #         return 1 if seats == 2 else 0
            
        #     res = 0
        #     if seats == 2:
        #         if corridor[i] == "S":
        #             res = dfs(i + 1, 1)
        #         else:
        #             res = (dfs(i + 1, 0) + dfs(i + 1, 2)) % mod
        #     else:
        #         if corridor[i] == "S":
        #             res = dfs(i + 1, seats + 1)
        #         else:
        #             res = dfs(i + 1, seats)
        #     return res
        # return dfs(0, 0)

        # time complexity: O(n)
        # space complexity: O(n)

        # mod = 10**9 + 7

        # seats = []
        # for i, c in enumerate(corridor):
        #     if c == "S": seats.append(i)

        # length = len(seats)
        # if length < 2 or length % 2 == 1:
        #     return 0

        # res = 1
        # i = 1
        # while i < length - 1:
        #     res = (res * (seats[i+1] - seats[i])) % mod
        #     i += 2
        # return res

        # time complexity: O(n)
        # space complexity: O(1)

        previous_seat_index = seats = 0
        count = 1

        for i, c in enumerate(corridor):
            if c == 'S':
                seats += 1

                if seats > 2 and seats & 1: 
                    count = (count * (i - previous_seat_index)) % (10 ** 9 + 7)

                previous_seat_index = i

        return count if seats and not seats & 1 else 0

