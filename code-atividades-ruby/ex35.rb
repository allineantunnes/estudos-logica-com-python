def add_element(list)
  list << 4
  puts "List inside function: #{list.inspect}"
end

my_list = [1, 2, 3]
add_element(my_list)
puts "List outside function: #{my_list.inspect}"
