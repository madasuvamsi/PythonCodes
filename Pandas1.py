__author__ = 'vamsi'
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")

web_stats={'Day':[1,2,3,4],
           'Visitors':[20,30,40,50],
           'Avg_Time':[2,10,11,20]}

df=pd.DataFrame(web_stats["Avg_Time"])
df.plot().hist()
# df=pd.DataFrame(web_stats)
# df._align_frame()
# df["Avg_Time"].plot()
# plt.title("Avg Time Spent on Website")
# plt.legend()
# plt.show()