months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]


def get_gradient_at_b(x, y, b, m):
    N = len(x)
    diff = 0

    for i in range(N):
        x_val = x[i]
        y_val = y[i]
        diff += y_val - ((m * x_val) + b)

    b_gradient = -(2 / N) * diff
    return b_gradient


def get_gradient_at_m(x, y, b, m):
    N = len(x)
    diff = 0

    for i in range(N):
        x_val = x[i]
        y_val = y[i]
        diff += x_val * (y_val - ((m * x_val) + b))

    m_gradient = -(2 / N) * diff
    return m_gradient


def step_gradient(x, y, b_current, m_current, learning_rate):
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)

    b = b_current - (learning_rate * b_gradient)
    m = m_current - (learning_rate * m_gradient)

    return b, m


def gradient_descent(x, y, learning_rate, num_iterations):
    b = 0
    m = 0

    for i in range(num_iterations):
        b, m = step_gradient(x, y, b, m, learning_rate)

    return b, m


def generate_b_values(learning_rate, num_iterations):
    b = 0
    m = 0
    b_values = []

    for i in range(num_iterations):
        b, m = step_gradient(months, revenue, b, m, learning_rate)
        b_values.append(b)

    return b_values


bs = generate_b_values(0.01, 1400)
bs_01 = generate_b_values(0.01, 100)
bs_000000001 = generate_b_values(0.000000001, 100)
