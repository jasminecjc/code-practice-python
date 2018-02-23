# -*- coding:utf-8 -*-


class QuickSort:
    def sort(self, start, end):
        if(start > end):
            return
        low, high = start, end
        base = self.arr[low]

        while start < end:
            while start < end and self.arr[end] >= base:
                end -= 1
            self.arr[start] = self.arr[end]
            while start < end and self.arr[start] <= base:
                start += 1
            self.arr[end] = self.arr[start]
        self.arr[start] = base
        self.sort(low, start - 1)
        self.sort(start + 1, high)

    def quickSort(self, A, n):
        self.arr = A
        self.sort(0, n - 1)
        return self.arr
