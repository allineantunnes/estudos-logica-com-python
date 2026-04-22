values = []
5.times do
  print 'Enter a value: '
  values << Integer(gets.chomp)
end

values.each_with_index do |value, index|
  puts "At position #{index} I found value #{value}!"
end
puts 'Reached the end of the list.'
