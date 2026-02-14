import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parametry
x = np.linspace(-2, 2, 400)

# Funkcja
def y_func(x, k):
    return np.cbrt(x**2) + 0.9 * np.sin(k * x) * np.sqrt(np.maximum(3 - x**2, 0))

# Tworzymy figurę z czarnym tłem
fig, ax = plt.subplots(facecolor='black')
ax.set_facecolor('black')

line, = ax.plot([], [], lw=2, color='red')  # wykres na czerwono
ax.set_xlim(-2, 2)
ax.set_ylim(-1.5, 2.5)

ax.axis('off')

# Inicjalizacja
def init():
    line.set_data([], [])
    return line,

# Funkcja animacji
def animate(frame):
    k = frame
    y = y_func(x, k)
    line.set_data(x, y)
    return line,

ani = FuncAnimation(fig, animate, init_func=init, frames=101, interval=100, blit=True)

plt.show()






