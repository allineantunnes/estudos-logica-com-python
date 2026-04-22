student_name = gets.chomp
grade1 = Integer(gets.chomp)
grade2 = Integer(gets.chomp)
grade3 = Integer(gets.chomp)
grade4 = Integer(gets.chomp)

first_weight = 2
second_weight = 3

weighted_average = (
  grade1 * first_weight +
  grade2 * first_weight +
  grade3 * second_weight +
  grade4 * second_weight
) / (first_weight * 2 + second_weight * 2).to_f

rounded_average = weighted_average.round

if rounded_average >= 60
  puts "Student #{student_name} got average #{rounded_average} and is approved."
elsif rounded_average >= 20
  puts "Student #{student_name} got average #{rounded_average} and is in recovery."
else
  puts "Student #{student_name} got average #{rounded_average} and is failed."
end
