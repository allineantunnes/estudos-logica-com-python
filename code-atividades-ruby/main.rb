require_relative 'calcArea'

def main
  puts 'Area calculation of geometric shapes:'
  puts '1. Circle'
  puts '2. Triangle'
  puts '3. Rectangle'

  begin
    print 'Which shape area do you want to calculate? '
    option = Integer(gets.chomp)

    if option < 1 || option > 3
      puts 'ERROR! This is not a valid option!'
    elsif option == 1
      print 'Enter circle radius: '
      radius = Float(gets.chomp)
      area = CalcArea.calculate_circle_area(radius)
      puts format('The circle area is: %.2f', area)
    elsif option == 2
      print 'Enter triangle base: '
      base = Float(gets.chomp)
      print 'Enter triangle height: '
      height = Float(gets.chomp)
      area = CalcArea.calculate_triangle_area(base, height)
      puts format('The triangle area is: %.2f', area)
    elsif option == 3
      print 'Enter rectangle width: '
      width = Float(gets.chomp)
      print 'Enter rectangle height: '
      height = Float(gets.chomp)
      area = CalcArea.calculate_rectangle_area(width, height)
      puts format('The rectangle area is: %.2f', area)
    end
  rescue ArgumentError
    puts 'ERROR! This is not a valid option!'
  end
end

main if __FILE__ == $PROGRAM_NAME
