print 'Enter a number: '
number = Integer(gets.chomp)

factorial = (1..number).reduce(1, :*)
puts "The factorial of this number is #{factorial}"
