def quick_sort(input_list):
    list_size = len(input_list)
    if list_size <= 1:
        return input_list
    mid_value = input_list.pop(list_size // 2)
    group_left = []
    group_right = []

    for i in range(list_size - 1):
        if input_list[i] < mid_value:
            group_left.append(input_list[i])
        else:
            group_right.append(input_list[i])
    return quick_sort(group_left) + [mid_value] + quick_sort(group_right)


sample_list = list(map(int, '32 5 16 2 3 99'.split(' ')))
print(quick_sort(sample_list))
