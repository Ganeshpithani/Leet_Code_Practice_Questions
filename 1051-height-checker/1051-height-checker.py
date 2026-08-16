class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ex=sorted(heights)
        c=0
        for i in range(len(heights)):
            if heights[i]!=ex[i]:
                c+=1
        return c        