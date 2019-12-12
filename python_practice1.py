# this is an free space to practice algo's


def add_one(num):
    return num + 1


def square_it(num):
    return num * num

def Quicksort(array):
    result = array.copy()
    first = array.shift()


def mergesort(array):

    return if len(array) <= 1
    mid = int(len(array) / 2)
    left = array[0:mid]
    right = array[mid:]

    return mergehelper(left, right)



def mergehelper(left,right):


def remove_the_vowels(string):
    result = ""
    vowel = "aeiou"
    for let in string:
        if !(vowel.includes(let)):
            result += let
    return result

def binarysearch(Array, target):
        return nil if len(Array) == 0

        mid = int(len(Array)/2)

        if Array[mid] == target:
                return mid
        else if Array[mid] < target:
                return binarysearch(Array[0:mid])
        else if Array[mid] > target:
                if Array[mid] == Nil:
                        return Nil
                else: 
                        return binarysearch(Array[mid:]) + 1 + mid

def caesar_cipher(str, shift):
  letters = ["a".."z"]

  encoded_str = ""
  for char in str:
    if char == " "
      encoded_str += " "
      next
    end
    old_idx = letters.find_index(char)
    new_idx = (old_idx + shift) % len(letters)

    encoded_str += letters[new_idx]
  end
  return encoded_str
end 

def deep_dup(arr):
  result = []
  for el in arr:
          if type(el) == "Array"
                result += deep_dup(el)
          else 
                result += el
  return result


def array_sort(arr):
        result = arr.sort()
        return result

def get_name(person):
        return preson.name

def count_to_three():
        print("one")
        sleep(1)
        print("two")
        sleep(1)
        print("three")

def taskmanager(tasks):

        # research assynchronous handling in python
        