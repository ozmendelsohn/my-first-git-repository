# let make a line!
from matplotlib import pyplot as plt
from matplotlib import use
import numpy as np
use('TkAgg')
x = np.arange(start=0, stop=2*np.pi, step=0.01)
y = np.sin(x)

plt.plot(x, y)
plt.title('This is Not a Line!')
plt.show()

