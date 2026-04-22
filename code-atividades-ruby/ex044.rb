def get_month(month)
  raise ArgumentError, 'Invalid month!' if month < 1 || month > 12

  puts month
end

get_month(Integer(gets.chomp))
