def merge_list_hw(home_list):
    if len(home_list) == 1:
        return home_list


def get_merge_sorted_list(unsorted_list):
    if len(unsorted_list) == 1:
        return unsorted_list
    
    mid_point = int((len(unsorted_list))//2)
    first_half = unsorted_list[:mid_point]
    second_half = unsorted_list[mid_point:]

    half_1 = get_merge_sorted_list(first_half)
    half_2 = get_merge_sorted_list(second_half)

    sorted_list = []
    i = j = 0
    while i < len(half_1) and j < len(half_2):
        if half_1[i] <= half_2[j]:
            sorted_list.append(half_1[i])
            i += 1
        else:
            sorted_list.append(half_2[j])
            j += 1

    sorted_list += half_1[i:]
    sorted_list += half_2[j:]

    return sorted_list


if __name__ == "__main__":
    unsorted_list = [7,11,4,10,21,24,23,14,18]
    print("Unsorted list:", unsorted_list)
    sorted_list = get_merge_sorted_list(unsorted_list)
    print("Sorted list:", sorted_list)

