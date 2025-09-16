

lst = [2, 5, 8, 3, 5, 8, 2, 96, 4, 7, 38]

def process_numbers(list):

  evens = []
  higher_than_avg = []
  avg_list = sum(list) / len(list)
  dict_val = dict()

  without_doubles = set(list)

  original_lst = [x for x in without_doubles]
  original_lst.sort()

  for x in original_lst:
    if x % 2 == 0:
      evens.append(x)
    if x > avg_list:
      higher_than_avg.append(x)
    
  dict_val["original"] = original_lst
  dict_val["evens"] = evens
  dict_val["greater_than_avg"] = higher_than_avg

  return dict_val


res = process_numbers(lst)

print(res)