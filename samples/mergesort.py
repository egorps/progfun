
def mergesort(l):
    if len(l) == 0 or len(l) == 1:
        return l
    mid = len(l) / 2
    return merge(mergesort(l[:mid]), mergesort(l[mid:]))
def merge(l1, l2):
    result = []
    while l1 and l2:
        if l1[0] < l2[0]:
            result.append(l1.pop(0))
        else:
            result.append(l2.pop(0))
    if l1 or l2:
        result.extend(l1) if l1 else result.extend(l2)
    return result

def quicksort(l):
    if len(l) == 0 or len(l) == 1:
        return l
    less = []
    equal = []
    greater = []
    pivot = l[ len(l)/2]
    for elem in l:
        if elem < pivot:
            less.append(elem)
        elif elem > pivot:
            greater.append(elem)
        else:
            equal.append(elem)

    return quicksort(less) + equal + quicksort(greater)

if __name__ == '__main__':
    l = [15,8,49,26,16,10,59,4]
    print "Sorting ", l
    print "MergeSort: ", mergesort(l)
    print "QuickSort: ", quicksort(l)
