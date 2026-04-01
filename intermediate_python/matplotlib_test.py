import matplotlib.pyplot as plt
import os
folder = "plots"
os.makedirs(folder, exist_ok=True)
year = [1950,1970,1990,2010]
pop =[2.519,3.692,5.263,6.972]
plt.plot(year,pop)
plt.title("World Population Growth")   #  figure title
plt.xlabel("Year")                     #  x-axis label
plt.ylabel("Population (Billions)")   #  y-axis label
plt.savefig(f"{folder}/population_plot.png")
plt.show()