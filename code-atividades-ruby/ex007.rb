sum = 0.0
(1..8).each do |index|
  print "Student grade #{index}: "
  grade = Float(gets.chomp)
  sum += grade
end

average = sum / 8
puts "The class average was #{average.round}"
