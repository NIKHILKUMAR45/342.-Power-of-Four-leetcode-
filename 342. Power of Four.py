def isPowerOfFour(n):
        ans=1
        d=0
        while ans <=n:
            ans= 4**d
            if  ans == n:
                return True
            else:
                 d+=1
        return False

n=16
print(isPowerOfFour(n))