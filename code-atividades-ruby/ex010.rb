source = 'rato'
result = ''

source.each_char do |char|
  result = char.upcase + result
end

puts result
