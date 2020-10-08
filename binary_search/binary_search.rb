# returns index of value in array

def binary_search(array, value)
  low = 0
  high = array.length
  middle = high / 2
  while high - 1 > low
    if array[middle] < value
      low = middle
    elsif array[middle] > value
      high = middle
    else
      return middle
    end
    middle = (low + high) / 2
  end
end

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
puts binary_search(a, 5) # should return 4
b = [1, 3, 8, 11, 15, 19, 29]
puts binary_search(b, 15) # should return 4
