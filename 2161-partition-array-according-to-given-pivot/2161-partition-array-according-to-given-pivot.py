class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        store = []
        store2 = []
        store3 = []

        for num in nums:
            if num < pivot:
                store.append(num)
            elif num == pivot:
                store2.append(num)
            else:
                store3.append(num)

        return store + store2 + store3