def get_gradient_at_b(x, y, m, b):
    diff = 0
    N = len(x)
    b_gradient = -2 / N

    for i in range(len(x)):
        diff += y[i] - (m * x[i] + b)

    return b_gradient * diff

# Example data
x = [1, 2, 3]
y = [5, 1, 3]

# Example line: y = mx + b
m = 1
b = 0

gradient_at_b = get_gradient_at_b(x, y, m, b)

print("Gradient at b:", gradient_at_b)
