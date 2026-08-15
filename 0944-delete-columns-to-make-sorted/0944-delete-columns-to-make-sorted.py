class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        c=0
        for col in range(len(strs[0])):
            i=""
            for row in range(len(strs)):
                i+=strs[row][col]
            s=sorted(i)
            r="".join(s)
            if i!=r:
                c+=1
        return c