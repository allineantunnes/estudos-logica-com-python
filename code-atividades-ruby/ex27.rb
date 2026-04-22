brazil = [
  ['Alisson', 1], ['Dani Alves', 2], ['Miranda', 3], ['Rodrigo Caio', 4],
  ['Casemiro', 5], ['Felipe Luis', 6], ['Taison', 7], ['R. Augusto', 8],
  ['Gabriel Jesus', 9], ['Neymar', 10], ['P. Coutinho', 11], ['Marcelo', 12],
  ['Marquinhos', 13], ['T. Silva', 14], ['Paulinho', 15]
]

loop do
  print 'Enter a number between 1 and 15: '
  number = Integer(gets.chomp)

  if number.between?(1, 15)
    player, shirt_number = brazil[number - 1]
    puts "Player #{player} wore shirt #{shirt_number} in this squad."
    break
  else
    print 'Number out of range. '
  end
end
