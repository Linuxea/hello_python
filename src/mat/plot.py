
import matplotlib.pyplot as pyplot

x = [x * x for x in range(1, 100) if x % 2 == 0]
x.append(100)
y = [y * y for y in range(1, 100) if y % 2 != 0]

pyplot.plot(x, y)

pyplot.show()
