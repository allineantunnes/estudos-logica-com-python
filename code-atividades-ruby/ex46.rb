def withdraw_money(value)
  available_notes = [50, 20, 10]

  if value < 10 || value > 600
    puts 'Invalid value. The amount must be between R$ 10.00 and R$ 600.00.'
    return
  end

  unless (value % 10).zero?
    puts 'Unable to withdraw this amount with the available notes!'
    return
  end

  puts 'PRINTING...'
  sleep(1)

  available_notes.each do |note|
    note_count = value / note
    value %= note
    sleep(1)
    puts "#{note_count} note(s) of R$ #{note}.00"
  end
end

print 'This ATM supports up to R$600.00 (notes: R$10.00, R$20.00, R$50.00). Enter amount: '
withdrawal_value = Integer(gets.chomp)
puts "Withdrawal amount R$ #{withdrawal_value}"

withdraw_money(withdrawal_value)
