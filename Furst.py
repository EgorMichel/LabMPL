import matplotlib.pyplot as plt
import os
import numpy as np
number_of_picture = 0
for data in os.listdir("dead_moroz"):
    figure, ax = plt.subplots()
    with open(os.path.join("dead_moroz", data)) as file:
        lines = file.readlines()
        for i in range(int(lines[0])):
            if int(lines[0]) < 100:
                point_size = 5
            else:
                point_size = 1
            ax.scatter(float(lines[i + 1].split()[0]), float(lines[i + 1].split()[1]), c='b', s=point_size)
        plt.title("Number of points: " + str(lines[0]))
        plt.axis('scaled')
        plt.savefig(str(number_of_picture) + ".png")
        number_of_picture += 1
