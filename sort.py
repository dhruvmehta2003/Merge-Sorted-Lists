def merge_sorted_lists(list1, list2):
    # Create a new empty list to hold the combined elements
    merged_list = []
    # Initialize indices for each input list
    i = 0
    j = 0
    # Iterate through both lists, comparing elements at the current index
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    # Append any remaining elements from the input lists
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    return merged_list
