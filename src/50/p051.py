# 병합 정렬
def merge_sort(input_list):
    list_size = len(input_list)
    if list_size <= 1:
        return input_list
    mid_val = list_size // 2
    group1 = merge_sort(input_list[:mid_val])
    group2 = merge_sort(input_list[mid_val:])
    result = []

    while group1 and group2:
        if group1[0] < group2[0]:
            result.append(group1.pop(0))
        else:
            result.append(group2.pop(0))

    while group1:
        result.append(group1.pop(0))
    while group2:
        result.append(group2.pop(0))
    return result


sample_list = [180, 145, 165, 45, 170, 175, 173, 171]
# 빈칸을 채워주세요

print(merge_sort(sample_list))
