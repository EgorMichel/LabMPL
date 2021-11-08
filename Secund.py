import numpy as np
import matplotlib.pyplot as plt

with open("Second/data.dat") as file:
    lines = [i.split() for i in file.readlines()]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            lines[i][j] = float(lines[i][j])

print(lines)
fig, axs = plt.subplots(3, 2, figsize=(7, 10))
plt.subplots_adjust(wspace=0.3, hspace=0.5)
cock = 0
for i in range(3):
    for j in range(2):
        axs[i, j].plot(lines[cock], lines[cock + 1])
        axs[i, j].grid(which='both')
        x_ticks = np.arange(0, 16, 2)
        y_ticks = np.arange(-10, 12, 2)
        axs[i, j].set_xticks(x_ticks)
        axs[i, j].set_yticks(y_ticks)
        axs[i, j].set_title('Frame ' + str(cock // 2))
        axs[i, j].set_xlim([min(lines[cock]), max(lines[cock])])
        axs[i, j].set_ylim([-10, 12])
        cock += 2

# ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
#
# color = 'tab:blue'
# ax2.set_ylabel('sin', color=color)  # we already handled the x-label with ax1
# ax2.plot(t, data2, color=color)
# ax2.tick_params(axis='y', labelcolor=color)
plt.savefig('Second_graph' + ".png")

plt.show()
