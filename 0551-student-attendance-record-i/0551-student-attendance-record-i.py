class Solution:
    def checkRecord(self, s: str) -> bool:
        Acount=0
        Lcount=0
        for i in s:
            if i=='A':
                Acount+=1
                Lcount=0
            elif i=='L':
                Lcount+=1
                if Lcount >=3:
                    return False
            else:
                Lcount=0
        else:
            if Acount <2:
                return True
            else:
                return False
                
                    