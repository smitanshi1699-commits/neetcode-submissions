class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        speed = right

        while left <= right:
            k = (left + right)//2

            total_time = 0

            for pile in piles:
                total_time += math.ceil(float(pile)/k)

            if total_time <= h:
                speed = k 
                right = k -1
            else :
                left = k +1
        return speed