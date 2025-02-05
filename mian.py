import nidaqmx
from itertools import count
import math
import pprint as pp
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
import time
import matplotlib.pyplot as plt
from nidaqmx.constants import TerminalConfiguration , READ_ALL_AVAILABLE


def update_plot1(frame, line, x, y, task):


    x=[i for i in range (1000)]

    y=task.read(number_of_samples_per_channel=1000)


    line.set_data(x, y)


    ax.set_xlim(0, len(x))
    #ax.autoscale_view()

    return line,


x = [0]
y = [0]


figure, ax = plt.subplots()
ax.set_ylim(0, 2)
ax.set_xlim(0, 1000)


line, = ax.plot(x, y, label="AI0")


with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan(
        "Dev1/ai8",
        terminal_config=TerminalConfiguration.RSE,
        min_val=-1.0,
        max_val=2.0
    )


    frame_gen1 = count(start=0, step=1)


    animation1 = FuncAnimation(
        figure,
        update_plot1,
        frames=frame_gen1,
        fargs=(line, x, y, task),
        interval=100,
        blit=False
    )

    plt.legend()
    plt.show()