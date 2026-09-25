class Solution:
    def maxArea(self, height: list[int]) -> int:
        m_a=0
        l,r=0,len(height)-1
        while l<r:
            h=min(height[l],height[r])
            w=r-l
            a=h*w
            m_a=max(a,m_a)
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return m_a