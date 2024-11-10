from typing import List

class Solution:
    def gcd(self, x, y):
        if y == 0:
            return x
        return self.gcd(y, x % y)

    def maxPoints(self, points: List[List[int]]) -> int:
        max_ = 0
        length = len(points)
        if length == 1:
            return 1

        for i in range(len(points)):
            grad = {}
            x0, y0 = points[i]
            local_max = 0

            for j in range(i + 1, len(points)):
                x, y = points[j]
                gcd_ = self.gcd(x - x0, y - y0)
                norm_slope = ((x - x0) // gcd_, (y - y0) // gcd_)
                
                if norm_slope not in grad:
                    grad[norm_slope] = 1
                grad[norm_slope] += 1
                
                local_max = max(local_max, grad[norm_slope])

            max_ = max(max_, local_max)

        return max_
