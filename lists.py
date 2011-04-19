squares = [ x**2 for x in range(10) if x % 2 == 0 ]
for x in squares:
    print x

last_three_squares = squares[-3::]
print last_three_squares
