class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        m_x=sum(nums[:k])
        w_x=m_x
        for i in range(k,len(nums)):
            w_x=w_x-nums[i-k]+nums[i]
            if w_x>m_x:
                m_x=w_x
            
        return m_x/k

        