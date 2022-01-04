class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        arr = []
        temp = []

        for el in arr2:
            if el in count:
                arr += ([el]*count[el])
                count.pop(el)

        for key in count:
            temp += [key] * count[key]

        arr.extend(sorted(temp))

        return arr
