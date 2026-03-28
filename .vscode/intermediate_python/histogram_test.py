import matplotlib.pyplot as plt
cgpa = [3.0,3.0,3.06,3.44,3.16,3.21,3.0,3.17,2.55]
#semester =[1,2,3,4,5,6,7,8,9]
plt.figure()
plt.hist(cgpa,bins=3)
plt.savefig("D:\DATACAMP\intro_to_Python\plots/histogram_plot.png")
plt.show()


plt.figure()
# Get histogram data
counts, bins, patches = plt.hist(cgpa, bins=3)

# Assign different colors to each bin
colors = ['red', 'green', 'blue']

for patch, color in zip(patches, colors):
    patch.set_facecolor(color)

plt.title("CGPA Histogram")
plt.xlabel("CGPA Range")
plt.ylabel("Frequency")
plt.savefig("D:\DATACAMP\intro_to_Python\plots/histogram_plot_color.png")
plt.show()