class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        store_left = []
        store_pivot = []
        store_right = []

        for num in nums:
            if num < pivot:
                store_left.append(num)
            elif num == pivot:
                store_pivot.append(num)
            else:
                store_right.append(num)

        return store_left + store_pivot + store_right