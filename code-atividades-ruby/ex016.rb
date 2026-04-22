withdrawal = Integer(gets.chomp)
while withdrawal < 1
  puts 'The informed amount must be at least 1.'
  withdrawal = Integer(gets.chomp)
end

valid_bills = [1, 2, 5, 10, 20, 50, 100]

max_bill = Integer(gets.chomp)
while !valid_bills.include?(max_bill)
  puts 'Invalid bill value. Enter a valid bill value.'
  max_bill = Integer(gets.chomp)
end

total = withdrawal
used_bills = []

puts "Withdrawn amount: R$ #{withdrawal}"
puts 'Bills:'

current_bill = max_bill
while total > 0
  if total >= current_bill
    bill_count = total / current_bill
    total -= bill_count * current_bill
    used_bills << [current_bill, bill_count]
  end

  current_bill = case current_bill
                 when 100 then 50
                 when 50 then 20
                 when 20 then 10
                 when 10 then 5
                 when 5 then 2
                 when 2 then 1
                 else 1
                 end
end

used_bills.each do |bill, quantity|
  puts "#{quantity} x R$ #{bill}"
end
