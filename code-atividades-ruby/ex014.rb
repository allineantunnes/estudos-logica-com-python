number = nil

loop do
  print 'Enter an integer greater than zero: '
  number = Integer(gets.chomp)
  break if number > 1
end

divisors = 0
(1..number).each do |value|
  divisors += 1 if (number % value).zero?
end

if divisors == 2
  puts "The number #{number} is prime"
else
  puts "The number #{number} has #{divisors} divisors, so it is not prime"
end
