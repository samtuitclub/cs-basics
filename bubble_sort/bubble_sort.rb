def bubble_sort(array)
  length = array.size
  return array if length <= 1
  
  while true
    swapped = false
    (length - 1).times do |i|
      if array[i] > array[i+1]
        array[i], array[i+1] = array[i+1], array[i]
        swapped = true
      end
    end

    break if not swapped
  end

  array
end

array = [56,3,2,5,6,7]
puts bubble_sort(array) # returns [2, 3, 5, 6, 7, 56]

