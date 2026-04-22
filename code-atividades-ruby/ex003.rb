num1 = Integer(gets.chomp)
num2 = Integer(gets.chomp)

predecessor = num1 - 1
successor = num1 + 1

double_value = num1 * 2
triple_value = num1 * 3
square_root = Math.sqrt(num1)
average = (num1 + num2) / 2.0

puts "The predecessor of number 1 is #{predecessor} and the successor is #{successor}. The double is #{double_value}, the triple is #{triple_value}, and its square root is #{square_root}."
puts "The average of the numbers is #{average}"
