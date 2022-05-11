result = []  
def merge_lists(list1, list2):

  if not list1:
    return list2
  if not list2:
    return list1
  if not list1 and not list2:
    return []
  
  if list1[0] < list2[0]:
    result.append(list1[0])
    merge_lists(list1[1:], list2)
  else:
    result.append(list2[0])
    merge_lists(list1, list2[1:])

  return result

print(merge_lists([1, 2, 4, 5], [1, 2, 4, 5, 6]))
