class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        m=max(heights)
        c=[0]*(m+1)
        for i in heights:
            i+=1
        r=[]
        for i in range(len(c)):
            r.extend([i]*c[i])
        r=sorted(heights)
        c=0
        for i in range(len(heights)):
            if heights[i]!=r[i]:
                c+=1
        return c        