teams = ['Flamengo', 'Fluminense', 'Botafogo', 'Vasco', 'America - RJ']

teams.each do |team1|
  teams.each do |team2|
    puts "#{team1} x #{team2}" if team1 != team2
  end
end
