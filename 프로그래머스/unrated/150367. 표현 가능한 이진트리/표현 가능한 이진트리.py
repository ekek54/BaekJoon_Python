def solution(numbers):
  result = []

  def one_exist(binary_tree, number_of_one):
    n = len(binary_tree)
    mid = n // 2
    if n == 1:
      if binary_tree[mid] == '1':
        number_of_one -= 1
      return number_of_one
    else:
      left = binary_tree[: mid]
      right = binary_tree[mid + 1:]
      if binary_tree[mid] == '1':
        number_of_one -= 1
        number_of_one = one_exist(left, number_of_one)
        number_of_one = one_exist(right, number_of_one)
      return number_of_one

  for number in numbers:
    binary_number_str = bin(number).lstrip('0b')
    depth = 1
    while 2 ** depth - 1 < len(binary_number_str):
      depth += 1
    complete_binary_tree = binary_number_str.zfill(2 ** depth - 1)
    number_of_one = complete_binary_tree.count('1')
    if one_exist(complete_binary_tree, number_of_one) == 0:
      result.append(1)
    else:
      result.append(0)
  return result