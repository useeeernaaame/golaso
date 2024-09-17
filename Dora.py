import matplotlib.pyplot as p
import numpy as n

size = 1000

x = n.linspace(0, size, size)
y=n.random.normal(0, 1, size)

p.plot(x ,y)
p.show