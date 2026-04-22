require 'net/http'
require 'uri'

uri = URI.parse('https://www.google.com.br')
response = Net::HTTP.get_response(uri)
puts response.code
