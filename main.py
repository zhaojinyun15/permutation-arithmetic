import random
import time

import permutation


def create_random_list(list_len):
    """
    生成随机数list
    :param list_len:
    :return:
    """
    if list_len < 0:
        raise Exception('params error!')
    if list_len > 100000:
        raise Exception('too long list!')
    max_num = list_len * 10
    random_list = []
    for i in range(list_len):
        random_list.append(random.randint(1, max_num))
        # yield random.randint(1, max_num)
    return random_list


if __name__ == '__main__':
    random_list = create_random_list(100000)
    # print(random_list)
    start_time = time.time()

    # permutation.bubble(random_list)
    # permutation.insertion(random_list)
    # permutation.merge(random_list, 0, len(random_list))
    # permutation.shell(random_list)
    permutation.heap(random_list)

    end_time = time.time()
    print(f'takes time: {(end_time - start_time) * 1000} ms')
    # print(random_list)
