def calculate_approximate_pi(precision):
    a = 0
    b = 1
    c = 1
    while True:
        d = 1 / b * c
        a += d
        b += 2
        c *= -1
        if abs(d) < precision:
            break
    return 4 * a


data = 1e-8
end = calculate_approximate_pi(data)
print(f"π的近似值: {end}")
