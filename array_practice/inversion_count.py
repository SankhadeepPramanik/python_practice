class Solution:
    def inversionCount(self, arr):
        self.count = 0
        self.merge_sort(arr)
        return self.count

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                # 🔥 Key line: count inversions
                self.count += (len(left) - i)
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result
s= Solution()
arr = [1, 20, 6, 4, 5]
print(s.inversionCount(arr))  # Output: 5




class Solution:
    def inversionCount1(self, arr):
        # Code Here
        return self.mergeSort(arr, 0, len(arr)-1)
        
    def merge(self, arr, low, mid, high):
        
        temp = []
        left, right = low, mid + 1
        
        count = 0
        
        while left <= mid and right <= high:

            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                count += (mid - left + 1)
                right += 1
        
        # add remaining elements from left & right
        while left <= mid:
            temp.append(arr[left])
            left += 1
        while right <= high:
            temp.append(arr[right])
            right += 1
        
        # copy temp result to orogonal array
        for i in range(low, high + 1):
            arr[i] = temp[i - low]
        
        return count
        
    
    def mergeSort(self, arr, low, high):
        
        total_count = 0
        
        if low >= high:
            return total_count
        
        mid = (low + high) // 2
        
        # collect count inversion from left & right half array
        total_count += self.mergeSort(arr, low, mid)
        total_count += self.mergeSort(arr, mid+1, high)
        
        total_count += self.merge(arr, low, mid, high)
        
        return total_count
s= Solution()
arr = [1, 20, 6, 4, 5, 7, 3, 5, 22, 75]
print(s.inversionCount1(arr))  # Output: 5