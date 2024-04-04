class ModifiedHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up()

    def pop_max(self):
        if not self.heap:
            return None

        self._swap(0, len(self.heap) - 1)
        max_value = self.heap.pop()
        self._heapify_down()

        return max_value

    def _heapify_up(self):
        current_index = len(self.heap) - 1
        while current_index > 0:
            parent_index = (current_index - 1) // 2
            if self.heap[current_index] > self.heap[parent_index]:
                self._swap(current_index, parent_index)
                current_index = parent_index
            else:
                break

    def _heapify_down(self):
        current_index = 0
        while True:
            left_child_index = 2 * current_index + 1
            right_child_index = 2 * current_index + 2
            max_index = current_index

            if (
                left_child_index < len(self.heap)
                and self.heap[left_child_index] > self.heap[max_index]
            ):
                max_index = left_child_index

            if (
                right_child_index < len(self.heap)
                and self.heap[right_child_index] > self.heap[max_index]
            ):
                max_index = right_child_index

            if max_index != current_index:
                self._swap(current_index, max_index)
                current_index = max_index
            else:
                break

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
