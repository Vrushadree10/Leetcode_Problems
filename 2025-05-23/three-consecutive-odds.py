class Solution(object):
    def threeConsecutiveOdds(self, arr):
        if len(arr) < 3:
            return False
        for i in range(1, len(arr)):
            if arr[i - 1] % 2 != 0 and arr[i] % 2 != 0:
                if (i + 1) < len(arr) and arr[i + 1] % 2 != 0:
                    return True
        return False
