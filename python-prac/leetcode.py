def array_rotation(mat,tar):
  for _ in range(4):
    if mat == tar:
      return True
    else:
      mat = [list(x) for x in zip(*mat[::-1])]
  return False

def subarray(arr,n,sum_):

  curr_sum = arr[0]
  i = 1
  start = 0

  while i <= 1:
    if curr_sum > sum_ and start <= i - 1:
      curr_sum = curr_sum - arr[start]
      start += 1


    if curr_sum == sum_:
      print (start , i-1)
      return 1


    if curr_sum < sum_:
      curr_sum += arr[i]
      i += 1

    return 0