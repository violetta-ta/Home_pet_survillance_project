import numpy as np
speeds = []
#Recording the values of speed in list, and then transforming it to np array
with open('log_speeds.txt', 'r') as reader:
    for line in reader.readlines():
        line.replace(".", ",")
        values = line.split()
        speeds.append(float(values[1]))
speeds_a = np.array(speeds)

#Print median and 98 percentile
print(np.median(speeds_a))
print(np.percentile(speeds_a, 98))
# Deleting the wrong readings, when the sensor interferred with the cage
array_reduced = speeds_a[speeds_a<200]
print(np.max(array_reduced))

#Plotting the statistics:
import matplotlib.pyplot as plt

p = np.linspace(0, 100, 6001)
graph = plt.gca()
for i in array_reduced:
    graph.plot(
        p, np.percentile(array_reduced, p),
         linestyle="-")
graph.set(
    title='Statistics for speeds' ,
    xlabel='Percentile',
    ylabel='Speed, cm/second')
    
graph.legend()
plt.show()
