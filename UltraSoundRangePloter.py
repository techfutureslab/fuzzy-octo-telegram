"""
A simple example of an animated plot
"""
import serial
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ser = serial.Serial('/dev/ttyACM0', 9600)


fig, ax = plt.subplots()
ax.set_ylim([0,50])
x = np.arange(0, 1500)
Y=[0]*1500
line, = ax.plot(x, np.sin(x))


def animate(i):
    data = ser.readline().rstrip()  # read data from serial
    print "data:", data
    #print i
    try:
        y = float(data)
    except:
        print data
        # exit()
        return 0
    Y[i%1500]=y
    print y
    line.set_ydata(Y)  # update the data
    return line,


# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

ani = animation.FuncAnimation(fig, animate, np.arange(1, 1500), init_func=init,
                              interval=25, blit=True)
plt.show()