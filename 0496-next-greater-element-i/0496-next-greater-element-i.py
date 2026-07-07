class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r=[]
        for i in range(len(nums1)):
            fd=False
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    for f in range(j+1,len(nums2)):
                        if nums2[f] > nums1[i]:
                            fd=True
                            r.append(nums2[f])
                            break
                    if not fd:
                        r.append(-1)
        return r

        