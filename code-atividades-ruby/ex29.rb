puts '=' * 40
puts 'Tabajara Supermarket'.center(40)
puts '=' * 40

products = []

loop do
  number = products.length + 1
  product_info = {}
  product_info['number'] = number

  print "Product #{number}: "
  product_info['name'] = gets.chomp
  print 'Price: '
  product_info['price'] = Float(gets.chomp)
  print 'Quantity: '
  product_info['qty'] = Integer(gets.chomp)
  product_info['total'] = product_info['price'] * product_info['qty']

  products << product_info

  print 'Do you want to add another product? Y/N: '
  continue_answer = gets.chomp.downcase

  if continue_answer == 'n'
    break
  elsif continue_answer != 'y'
    print 'Type again! '
  end
end

puts '=' * 40
puts 'Confirmation and Removal'.center(40)
puts '=' * 40

loop do
  print 'Do you want to remove any product? Y/N: '
  remove_answer = gets.chomp.downcase
  break if remove_answer == 'n'
  next unless remove_answer == 'y'

  print 'What is the product number? '
  product_number = Integer(gets.chomp)

  found_product = products.find { |product| product['number'] == product_number }

  if found_product
    products.delete(found_product)
    puts "Item #{found_product['name']} removed!"
  else
    puts 'Item not found'
  end
end

puts '=' * 50
puts 'Purchase Summary'.center(50)
puts '=' * 50

total_purchases = 0.0
puts format('%-5s %-15s %-10s %-10s %-10s', 'No', 'Product', 'Price', 'Qty', 'Total')

products.each do |product|
  number = product['number']
  name = product['name']
  price = product['price']
  qty = product['qty']
  total = product['total']

  total_purchases += total
  puts format('%-5d %-15s %-10.2f %-10d %-10.2f', number, name, price, qty, total)
end

puts format("\nTotal: %25.2f", total_purchases)
