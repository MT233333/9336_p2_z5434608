import math
import matplotlib.pyplot as plt
import numpy as np

def path_loss(distance, frequency):
    c = 300000000 # light speed
    loss = 20 * math.log10(distance) + 20 * math.log10(frequency) + 20 * math.log10(4 * math.pi / c)
    return loss



# set distance from 1 to 50 meters
distance = np.arange(1, 51, 1)

# calculate path loss at 2.4 GHz and 5 GHz
loss_2p4ghz = [path_loss(d, 2.4 * 10**9) for d in distance]
loss_5ghz = [path_loss(d, 5 * 10**9) for d in distance]


# draw the figure
plt.plot(distance, loss_2p4ghz, label='2.4 GHz')
plt.plot(distance, loss_5ghz, label='5 GHz')
plt.xlabel('Distance (m)')
plt.ylabel('Path Loss (dB)')
plt.title('Path Loss at 2.4 GHz and 5 GHz')
plt.legend()
plt.show()