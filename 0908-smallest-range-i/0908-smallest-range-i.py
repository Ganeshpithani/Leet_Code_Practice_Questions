class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        maximum = max(nums)
        minimum = min(nums)

        score = maximum - minimum - (2 * k)

        if score < 0:
            return 0

        return score
        