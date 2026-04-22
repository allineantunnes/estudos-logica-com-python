sum = 0.0
quantity = 1

while quantity <= 8
  print "Student grade #{quantity}: "
  grade = Float(gets.chomp)
  sum += grade
  quantity += 1
end

average = sum / 8
puts "The class average was #{average.round}"
