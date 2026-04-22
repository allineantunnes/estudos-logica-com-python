list = [1, 2, 3, 4, 5]
sum = 0

list.each do |value|
  if value.even?
    sum += value
  else
    sum -= value
  end
end

puts sum
