
def swap(origin_list, index1, index2):
    temp = origin_list[index1]
    origin_list[index1] = origin_list[index2]
    origin_list[index2] = temp


def bubble(origin_list):
    """
    N^2
    :param origin_list:
    :return:
    """
    for i in range(len(origin_list)):
        j = len(origin_list) - 1
        while j > i:
            num2 = origin_list[j]
            num1 = origin_list[j - 1]
            if num1 > num2:
                swap(origin_list, j, j-1)
            j -= 1
    return origin_list


def insertion(origin_list):
    """
    N^2
    :param origin_list:
    :return:
    """
    for i in range(1, len(origin_list)):
        temp = origin_list[i]
        j = i
        while j > 0 and origin_list[j - 1] > temp:
            origin_list[j] = origin_list[j - 1]
            j -= 1
        origin_list[j] = temp
    return origin_list


def merge(origin_list, begin_index, end_index):
    """
    NlogN
    :param origin_list:
    :param begin_index:
    :param end_index:
    :return:
    """
    if begin_index >= end_index:
        return origin_list
    half_index = (begin_index + end_index) // 2
    # do left
    merge(origin_list, begin_index, half_index)
    # do right
    merge(origin_list, half_index + 1, end_index)
    # merge left and right
    left_index, right_index, origin_index = 0, 0, begin_index
    left_list = origin_list[begin_index: half_index + 1].copy()
    right_list = origin_list[half_index + 1: end_index + 1].copy()
    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] <= right_list[right_index]:
            origin_list[origin_index] = left_list[left_index]
            left_index += 1
        else:
            origin_list[origin_index] = right_list[right_index]
            right_index += 1
        origin_index += 1
    while left_index < len(left_list):
        origin_list[origin_index] = left_list[left_index]
        left_index += 1
        origin_index += 1
    while right_index < len(right_list):
        origin_list[origin_index] = right_list[right_index]
        right_index += 1
        origin_index += 1
    return origin_list


def shell(origin_list):
    """
    N^(3/2)
    :param origin_list:
    :return:
    """
    list_length = len(origin_list)
    gap = list_length // 2
    while gap >= 1:
        for i in range(gap, list_length):
            j = i
            temp = origin_list[j]
            while j > 0 and origin_list[j - gap] > temp:
                origin_list[j] = origin_list[j - gap]
                j -= gap
            origin_list[j] = temp
        gap //= 2
    return origin_list


def prec_down(origin_list, i, last_index):
    """
    for heap sort, percolate down the element of index i
    :param origin_list:
    :param i:
    :param last_index:
    :return:
    """
    child_index = i * 2 + 1
    while child_index <= last_index:
        if child_index != last_index and origin_list[child_index] < origin_list[child_index + 1]:
            child_index += 1
        if origin_list[i] < origin_list[child_index]:
            swap(origin_list, i, child_index)
        else:
            break
        i = child_index
        child_index = i * 2 + 1


def heap(origin_list):
    """
    NlogN
    :param origin_list:
    :return:
    """
    if len(origin_list) < 2:
        return origin_list
    # build heap
    i = len(origin_list) // 2 - 1
    while i >= 0:
        prec_down(origin_list, i, len(origin_list) - 1)
        i -= 1
    # delete max
    i = len(origin_list) - 1
    while i > 0:
        swap(origin_list, 0, i)
        prec_down(origin_list, 0, i - 1)
        i -= 1
    return origin_list


def medium3(origin_list, left_index, right_index):
    """
    choose a pivot of quick sort
    :param origin_list:
    :param left_index:
    :param right_index:
    :return:
    """
    center_index = (left_index + right_index) // 2
    if origin_list[left_index] > origin_list[center_index]:
        swap(origin_list, left_index, center_index)
    if origin_list[left_index] > origin_list[right_index]:
        swap(origin_list, left_index, right_index)
    if origin_list[center_index] > origin_list[right_index]:
        swap(origin_list, center_index, right_index)
    swap(origin_list, center_index, right_index - 1)
    return origin_list[right_index - 1]


def quick(origin_list, left_index, right_index):
    """
    NlogN
    :param origin_list:
    :param left_index:
    :param right_index:
    :return:
    """
    if right_index - left_index < 1:
        return origin_list
    if right_index - left_index <= 2:
        medium3(origin_list, left_index, right_index)
        return origin_list
    pivot = medium3(origin_list, left_index, right_index)
    i = left_index + 1
    j = right_index - 2
    while True:
        while origin_list[i] < pivot:
            i += 1
        while origin_list[j] > pivot:
            j -= 1
        if i < j:
            swap(origin_list, i, j)
            i += 1
            j -= 1
        else:
            break
    swap(origin_list, i, right_index - 1)
    quick(origin_list, left_index, i - 1)
    quick(origin_list, i + 1, right_index)
    return origin_list
