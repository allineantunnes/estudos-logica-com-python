dictionary = { 'a' => 1, 'b' => 2, 'c' => 3 }
sum = 0

dictionary.each_value do |value|
  if value.even?
    sum += value
  else
    sum -= value
  end
end

puts sum
