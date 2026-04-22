values = []
values << 8
values << 16
values << 32

values.each_with_index do |value, index|
  puts "At position #{index} I found value #{value}"
end
puts 'Reached the end of the list!'
