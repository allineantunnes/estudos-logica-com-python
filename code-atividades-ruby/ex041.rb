def print_max(a, b)
  if a > b
    puts "#{a} is greater"
  elsif a == b
    puts "#{a} is equal to #{b}"
  else
    puts "#{b} is greater"
  end
end

print_max(3, 4)
