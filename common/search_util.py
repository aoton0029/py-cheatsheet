class SearchAlgorithm:
    @staticmethod
    def binary_search(data, value):
        left = 0
        right = len(data) - 1
        while left <= right:
            mid = (left + right) // 2
            if data[mid] == value:
                return mid
            elif data[mid] < value:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    @staticmethod
    def bubble_sort(data):
        change = True
        for i in range(len(data)):
            if not change:
                break
            change = False
            for j in range(len(data) - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    change = True
        return data

    @staticmethod
    def linear_search(data, value):
        for i in range(len(data)):
            if data[i] == value:
                return i
        return -1

    @staticmethod
    def insertion_sort(data):
        for i in range(1, len(data)):
            j = i
            while j > 0 and data[j] < data[j - 1]:
                data[j], data[j - 1] = data[j - 1], data[j]
                j -= 1
        return data

    @staticmethod
    def selection_sort(data):
        for i in range(len(data)):
            min_index = i
            for j in range(i + 1, len(data)):
                if data[j] < data[min_index]:
                    min_index = j
            data[i], data[min_index] = data[min_index], data[i]
        return data

    @staticmethod
    def quick_sort(data):
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return SearchAlgorithm.quick_sort(left) + middle + SearchAlgorithm.quick_sort(right)

    @staticmethod
    def merge_sort(data):
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]
        return SearchAlgorithm.merge(SearchAlgorithm.merge_sort(left), SearchAlgorithm.merge_sort(right))

    @staticmethod
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result

    @staticmethod
    def heap_sort(data):
        import heapq
        heapq.heapify(data)
        return [heapq.heappop(data) for _ in range(len(data))]