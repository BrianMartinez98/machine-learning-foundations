def get_gradient_at_b(x, y, m, b):
    diff = 0
    N = len(x)

    for i in range(N):
        y_val = y[i]
        x_val = x[i]
        diff += y_val - ((m * x_val) + b)

    b_gradient = -2 / N * diff
    return b_gradient


def get_gradient_at_m(x, y, m, b):
    diff = 0
    N = len(x)

    for i in range(N):
        y_val = y[i]
        x_val = x[i]
        diff += x_val * (y_val - ((m * x_val) + b))

    m_gradient = -2 / N * diff
    return m_gradient

# Example data
x = [1, 2, 3]
y = [5, 1, 3]

# Example line: y = mx + b
m = 1
b = 0

b_gradient = get_gradient_at_b(x, y, m, b)
m_gradient = get_gradient_at_m(x, y, m, b)

print("Gradient at b:", b_gradient)
print("Gradient at m:", m_gradient)
