import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
frequency=10
sampling_rate=1000
t = np.linspace(0, 1 / frequency, int(sampling_rate / frequency), endpoint=False)
pulse = 1.65 + 1.65 * signal.square((2 * np.pi * frequency*t), duty=0.2)
plt.plot(t, pulse)

plt.show()