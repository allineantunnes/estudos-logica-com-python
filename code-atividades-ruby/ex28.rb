loop do
  products = []

  puts '=' * 40
  puts 'Tabajara Supermarket'.center(40)
  puts '=' * 40

  product_number = 1

  loop do
    product_info = {}
    print "Product #{product_number}: "
    product_info['name'] = gets.chomp
    print 'Price: '
    product_info['price'] = Float(gets.chomp)
    print 'Quantity: '
    product_info['quantity'] = Integer(gets.chomp)
    product_info['number'] = product_number
    product_info['total'] = product_info['price'] * product_info['quantity']

    products << product_info

    print 'Do you want to add another product? Y/N: '
    response = gets.chomp.downcase
    break unless response == 'y'

    product_number += 1
  end

  puts '=' * 40
  puts 'Confirmation and Removal'.center(40)
  puts '=' * 40

  loop do
    print 'Do you want to remove any product? Y/N: '
    remove = gets.chomp.downcase
    break if remove == 'n'
    next unless remove == 'y'

    print 'What is the product number? '
    product_number_to_remove = Integer(gets.chomp)

    found_product = products.find { |product| product['number'] == product_number_to_remove }

    if found_product
      products.delete(found_product)
      puts "Item #{found_product['name']} removed!"
    else
      puts 'Item not found'
    end
  end

  puts '=' * 40
  puts 'Purchase Summary'.center(40)
  puts '=' * 40

  total_purchases = 0.0

  puts format('%-5s%-10s%-10s%-10s%-10s', 'No', 'Product', 'Price', 'Qty', 'Total')
  products.each do |product|
    puts format('%-5d%-10s%-10.2f%-10d%-10.2f', product['number'], product['name'], product['price'], product['quantity'], product['total'])
    total_purchases += product['total']
  end

  puts format('%35s%.2f', '--> ', total_purchases)

  print 'Do you want to make another purchase? Y/N: '
  final_response = gets.chomp.downcase
  break unless final_response == 'y'
end
