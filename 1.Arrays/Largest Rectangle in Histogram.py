class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.sort()
        a=heights
        b=list(set(a))
     
        c1=a.count(b[-1])
        c2=a.count(b[-2])
        return (b[-2]*(c1+c2))
