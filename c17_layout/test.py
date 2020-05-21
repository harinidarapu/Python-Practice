from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle

# Your data
a = ([126, 237, 116, 15, 136, 348, 227, 247, 106, 5, -96, 25, 146],
     [117, 127, 228, 107, 6, 137, 238, 16, 339, 218, 97, -4, -105])

# Your scatter plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(a[0], a[1], color = 'red', s=10)

# Add rectangles
#width = 30
#height = 20
#a_zipped = zip(*a)
#for a_x, a_y in a_zipped:
#    ax.add_patch(Rectangle(xy=(a_x, a_y),width=width, height=height, linewidth=1, color='blue', fill=False))
#ax.axis('equal')
plt.show()