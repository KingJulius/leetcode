#User function Template for python3
class Solution:
	def matSearch(self,mat, N, M, X):
		# Complete this function
		i, j = 0, M-1
		while (0 <= i and i <= N-1) and (0 <= j and j <= M-1):
		    if mat[i][j] == X:
		        return 1
		    elif X < mat[i][j]:
		        j -= 1
		    elif mat[i][j] < X:
		        i += 1
		return 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        arr = [int(x) for x in input().split()]
        x = int(input())
        mat = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                mat[i][j] = arr[i * m + j]
        ob = Solution()
        print(ob.matSearch(mat, n, m, x))
# } Driver Code Ends