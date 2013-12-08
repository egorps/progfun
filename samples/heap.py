from math import ceil
import random
import datetime

class MaxHeap(object):
    def __init__(self):
        self.array = []

    def add_elem(self, elem):
        new_index = len(self.array)
        self.array.append(elem)
        self._bubble_up(new_index)

    def remove_head(self):
        head = self.array[0]
        self.array[0] = self.array[len(self.array)-1]
        self.array = self.array[:-1]
        if len(self.array) != 0:
            self._bubble_down(0)
        return head

    def _bubble_up(self, n):
        if n == 0:
            return
        parent_n = self._parent_index(n)
        parent = self.array[parent_n]
        elem = self.array[n]
        if parent < elem:
            self.array[parent_n] = elem
            self.array[n] = parent
            self._bubble_up(parent_n)

    def _bubble_down(self, n):
        elem = self.array[n]
        (max, max_idx) = self._max_child(n)
        if not max:
            return
        if max > elem:
            self.array[n] = max
            self.array[max_idx] = elem
            self._bubble_down(max_idx)

    def _max_child(self, n):
        young_child_idx = self._young_child(n)
        old_child_idx = self._old_child(n)
        young = self.array[young_child_idx] if young_child_idx < len(self.array) else None
        old = self.array[old_child_idx] if old_child_idx < len(self.array) else None
        if not old or not young:
            return (young, young_child_idx) if young else (old, old_child_idx) # returns the non-none child, or none if both are none
        return (old, old_child_idx) if old > young else (young, young_child_idx)

    def _parent_index(self, n):
        if n == 0:
            return n
        return int(ceil(n/2.0)-1)

    def _young_child(self, n):
        return (2 * ( n+1 ) ) - 1

    def _old_child(self, n):
        return 2 * (n+1)

    def __repr__(self):
        return str(self.array)

    def sort(self):
        while len(self.array) > 0:
            yield self.remove_head()

if __name__ == '__main__':
    random.seed(datetime.datetime.now())
    heap = MaxHeap()
    for x in xrange(20):
        heap.add_elem(random.randint(0, 1000))
    print "Heap: ", heap
    print "Sorted Array: ", [e for e in heap.sort()]


