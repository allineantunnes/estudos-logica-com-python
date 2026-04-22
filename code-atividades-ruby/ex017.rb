numbers_tuple = [2, 8, 6, 9, 10].freeze
numbers = [2, 8, 6, 9, 10]

numbers[2] = 3
numbers << 7
numbers.sort!
numbers.insert(2, 0)

if numbers.include?(4)
  numbers.delete(4)
else
  puts 'Could not find number 4'
end

puts numbers.inspect
puts "This list has #{numbers.length} elements"
puts numbers_tuple.inspect
