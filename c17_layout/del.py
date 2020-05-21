import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame([[5.1, 3.5], [4.9, 3.0], [7.0, 3.2],
                   [6.4, 3.2], [5.9, 3.0]],
                  columns=['length', 'width'])
ax1 = df.plot.scatter(x='length',
                      y='width' )
plt.show()