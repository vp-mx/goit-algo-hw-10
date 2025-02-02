import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

N = 10000000
max_y = 4
# Генерація точок [a, b] x [0, max_y]
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, max_y, N)
# Кількість точок, що знаходяться під кривою f(x)
points_under_curve = np.sum(y_random < f(x_random))
rectangle_area = (b - a) * max_y

integral_estimate = (points_under_curve / N) * rectangle_area
print("Monte Carlo estimate of the integral:", integral_estimate)

# scipy.integrate.quad рахує точне значення
result, *_ = spi.quad(f, a=a, b=b)
print("Quad integration result:", result)
print("Absolute error in Monte Carlo method:", abs(result - integral_estimate))

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Випадкові точки для оцінки інтегралу
sample_indices = np.random.choice(N, size=1000, replace=False)
ax.scatter(x_random[sample_indices], y_random[sample_indices], s=1, color='blue', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
