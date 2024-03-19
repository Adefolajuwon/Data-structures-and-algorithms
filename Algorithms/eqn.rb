def solve_quadratic
    print "Enter coefficient a: "
    a = gets.chomp.to_f
  
    print "Enter coefficient b: "
    b = gets.chomp.to_f
  
    print "Enter coefficient c: "
    c = gets.chomp.to_f
  
    discriminant = b**2 - 4*a*c
  
    if discriminant > 0
      root1 = (-b + Math.sqrt(discriminant)) / (2*a)
      root2 = (-b - Math.sqrt(discriminant)) / (2*a)
      return [root1, root2]
    elsif discriminant == 0
      root = -b / (2*a)
      return [root]
    else
      return []  # No real roots
    end
  end
  
  # Example usage
  roots = solve_quadratic
  if roots.empty?
    puts "No real roots"
  else
    puts "Roots: #{roots.join(', ')}"
  end
  