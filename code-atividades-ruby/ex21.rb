list1 = [[1, 2], [3, 4], [5, 6]]
list2 = []

list1.each do |inner|
  inner.each do |value|
    list2 << value
  end
end

puts list2.inspect
