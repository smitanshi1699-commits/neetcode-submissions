class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        top_letters = [letter for letter, count in freq.most_common(k)]
        return top_letters