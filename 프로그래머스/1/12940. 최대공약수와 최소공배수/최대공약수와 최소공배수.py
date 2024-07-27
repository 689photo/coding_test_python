def solution(n, m):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    def lcm(x, y):
        return x * y //gcd(x, y)
    
    return (gcd(n, m), lcm(n, m))