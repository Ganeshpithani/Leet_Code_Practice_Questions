class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        n=len(s)
        r=[]
        for i in range(n):
            r.append(s)
            s=s[1:]+s[0]
        for j in r:
            if j==goal:
                return True
        return False