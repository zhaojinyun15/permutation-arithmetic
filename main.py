import random
import time


def create_random_list(list_len):
    """
    生成随机数list
    :param list_len:
    :return:
    """
    if list_len < 0:
        raise Exception('params error!')
    if list_len > 1000000:
        raise Exception('too long list!')
    max_num = list_len * 10
    random_list = []
    for i in range(list_len):
        random_list.append(random.randint(1, max_num))
        # yield random.randint(1, max_num)
    return random_list


if __name__ == '__main__':
    start_time = time.time()
    random_list = create_random_list(100)
    print(random_list)
    end_time = time.time()
    print(f'takes time: {end_time - start_time} seconds')
