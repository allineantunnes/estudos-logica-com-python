module CalcArea
  def self.calculate_circle_area(radius)
    Math::PI * (radius**2)
  end

  def self.calculate_triangle_area(base, height)
    (base * height) / 2.0
  end

  def self.calculate_rectangle_area(width, height)
    width * height
  end
end
