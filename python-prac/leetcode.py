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


def targetIndices(self, nums: List[int], target: int) -> List[int]:
        new = sorted(nums)
        counter = 0
        ids = []
        for i in new:
            if i == target:
                ids.append(new.index(i) + counter)
                counter += 1

        return ids

def reverseWords(self, s: str) -> str:
        def reverse_array(arr):
            start , end = 0 , len(arr)-1
            while start < end:
                arr[start], arr[end] = arr[end] , arr[start]
                start += 1
                end -= 1

            return(arr)
        s = s + " "
        words = []
        start = 0
        end = 0
        for i in range(len(s)):
            if s[i] ==  " ":
                word = s[start:i]
    
                words.append(word)
                start = i+1



        new_words = reverse_array(words)


        new_s = ""
        for word in new_words:
            new_s = new_s + word
            new_s = new_s + " "

        new_s = new_s[:-1]

        return new_s