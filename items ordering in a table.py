
# You are given a number from 2 to N + 1 you have to order items in 2D table using the following rules 
# 1) go through the number in ascending order 
# 2) if the current number I satisfies gcd(i,j) = 1 for all j belongs to {2.....,i-1} then put it at the beginning ( the first cell) of the first unused row otherwise put it at the first unused cell of the row of minimum number j satisfies gcd(i,j)!=1 
#  you have to calculate the product of R*C where R is the row of N + 1 and C is its column
n = int(input())
import math
class Solution():
    
    def ifSatisfies(self,i):
        ctr=0
        for j in range(2,i):
            
            if math.gcd(i,j)!=1:
                return ctr
            ctr+=1
        return True
    def solve(self, n):
        self.final = 0
        
        self.ans=[]
        for i in range(2,n+2):
            ctr=1
            temp = self.ifSatisfies(i)
            if(temp==True):
                self.ans.append([i])
                if i==(n+2)-1:
                    self.final = ctr*len(self.ans[-1])
                
                
            else:
                self.ans[temp].append(i)
                self.final = (temp+1)*len(self.ans[temp])
            ctr+=1
        print(self.ans)
        return self.final
                
                
        
print(Solution().solve(n))
# 2 3 4 5 6  
        
