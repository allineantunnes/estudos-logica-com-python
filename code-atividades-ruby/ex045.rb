def external(a, b)
  internal = lambda do |c, d|
    c + d
  end

  internal.call(a, b)
end

result = external(5, 10)
puts result
