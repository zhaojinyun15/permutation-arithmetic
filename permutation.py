
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
