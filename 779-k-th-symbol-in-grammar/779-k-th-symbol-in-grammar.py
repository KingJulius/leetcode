class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1 and k==1:
            return 0
        m = (2**(n-1))//2
        if k <= m:
            return self.kthGrammar(n-1, k)
        else:
            return 0 if self.kthGrammar(n-1, k-m)==1 else 1