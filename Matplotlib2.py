__author__ = 'vamsi'
import matplotlib.pyplot as plt

x1=[1,2,3]
y1=[5,8,4]

x2=[1,2,3]
y2=[11,15,12]

plt.plot(x1,y1,label="First Line")
plt.plot(x2,y2,label="Second Line")
plt.xlabel("Plot Numbers")
plt.ylabel("Important Values")
plt.title("Interesting Graph")
plt.legend()
plt.show()