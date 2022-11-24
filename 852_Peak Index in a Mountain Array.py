class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1
        m = int(l - (l - r) / 2)
        while (arr[m] < arr[m-1]) or (arr[m] < arr[m+1]):
            if arr[m] < arr[m+1]:
                l = m
            if arr[m] < arr[m-1]:
                r = m
            m = int(l - (l - r) / 2)
        return m