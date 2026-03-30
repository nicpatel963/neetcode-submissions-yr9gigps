class Solution:
    MIN_RUN = 4

    def insertion_sort(self, arr, left, right):
        """Standard insertion sort for small chunks."""
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def merge(self, arr, l, m, r):
        """Standard merge logic from Merge Sort."""
        len1, len2 = m - l + 1, r - m
        left, right = [], []
        for i in range(0, len1):
            left.append(arr[l + i])
        for i in range(0, len2):
            right.append(arr[m + 1 + i])

        i, j, k = 0, 0, l
        while i < len1 and j < len2:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len1:
            arr[k] = left[i]
            k += 1
            i += 1
        while j < len2:
            arr[k] = right[j]
            k += 1
            j += 1

    def sortArray(self, nums):
        n = len(nums)

        # 1. Sort individual runs of size MIN_RUN
        for i in range(0, n, self.MIN_RUN):
            self.insertion_sort(nums, i, min((i + self.MIN_RUN - 1), n - 1))

        # 2. Start merging from size MIN_RUN. It will merge 32, then 64, 128...
        size = self.MIN_RUN
        while size < n:
            for left in range(0, n, 2 * size):
                mid = min(n - 1, left + size - 1)
                right = min((left + 2 * size - 1), (n - 1))

                if mid < right:
                    self.merge(nums, left, mid, right)
            size *= 2
        
        return nums
