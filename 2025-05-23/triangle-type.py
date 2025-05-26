class Solution(object):
    def triangleType(self, arr):
        if len(arr) != 3:
            return "none"
        
        a, b, c = sorted(arr)
        
        if a + b <= c:
            return "none"
        if a == b == c:
            return "equilateral"
        elif a == b or b == c or a == c:
            return "isosceles"
        else:
            return "scalene"
