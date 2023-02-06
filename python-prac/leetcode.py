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

from collections import Counter
def create_note(ransomNote,magazine):

    m = collections.Counter(magazine)
    for letter in ransomNote:
        if m[letter] != 0 and letter in m:
            m[letter] -= 1
        else:
            return False

def mySqrt(self, x: int) -> int:
    """start a while loop, find mid 
    """
        low = 0 
        high = x 

        while low <= high:
            mid = (low+high)//2

            if (mid * mid) > x:
                high = mid -1
            elif (mid * mid) < x:
                low = mid + 1

            else:
                return mid 

        return high

s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"

def areNumbersAscending(s: str) -> bool:
        

        str_numbers = []
        new = s.split()
        for i in range(len(new)):
            if new[i] != " ":
                if new[i].isdigit():
                    str_numbers.append(int(new[i]))
                    print(str_numbers)

        print("ok", set(sorted(str_numbers)))
        if str_numbers == list(set(sorted(str_numbers))):
            print('yes')
            return True

def areNumbersAscending(self, s: str) -> bool:
        previous_number = 0

        list_s = s.split()
        for w in list_s:
            if w.isnumeric():
                if previous_number >= int(w):
                    return False
                else:
                    previous_number = int(w)

        return True

def islandPerimeter(self, grid: List[List[int]]) -> int:
        tp , bp , lp , rp = 0 , 0 , 0 , 0
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for cube in range(cols): 
                if grid[row][cube] == 1:
                #check top
                    if row == 0 or grid[row-1][cube] == 0: 
                        tp +=1

                #check right
                    if cube == cols -1 or grid[row][cube+1] == 0:
                        rp += 1

                #check left
                    if cube == 0 or grid[row][cube-1] ==0:
                        lp +=1

                #check bottom
                    if row == rows - 1 or grid[row+1][cube] == 0:
                        bp += 1

        p = tp + bp + lp + rp

        return p


def findlength(a: str, b: str) -> int:
        a_l = [ord(chr) for chr in a]
        b_l = [ord(chr) for chr in b]

        idx = 0

        a_l = sorted(a_l)
        b_l = sorted(b_l)
        print(a_l,b_l)
        for i,j in zip(a_l,b_l):
            if i == j:
                idx += 1
            else:
                break
        print(idx, len(a_l))
        if idx == len(a_l) and idx == len(b_l):
            print(idx, a_l, b_l)
            return -1
        if idx > 0:
            return max((len(a_l)-idx),(len(b_l)-idx))
    
        else:
            return max(len(a_l), len(b_l))

def calPoints(operations) -> int:
        stack = []
        for i in operations:
            if i == "C":
                stack.pop()
            elif i == "D":
                stack.append(stack[-1] * 2)

            elif i == "+":
                stack.append(stack[-1] + stack[-2])

            else:
                print(int(i))
                stack.append(int(i))

        return sum(stack)