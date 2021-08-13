
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
    NlogN
    :param origin_list:
    :return:
    """
    list_length = len(origin_list)
    gap = list_length // 2
    while gap >= 1:
        i = gap
        while i < list_length:
            j = i
            temp = origin_list[j]
            while j > 0 and origin_list[j - gap] > temp:
                origin_list[j] = origin_list[j - gap]
                j -= gap
            origin_list[j] = temp
            i += 1
        gap //= 2
