import matplotlib.pyplot as plt
cgpa = [3.0,3.0,3.06,3.44,3.16,3.21,3.0,3.17,2.55]
semester =[1,2,3,4,5,6,7,8,9]
plt.figure()
plt.title("Alif you stupid dump ass. look what you did")
plt.xlabel("By_semester")
plt.ylabel("cgpa_result")
plt.plot(semester,cgpa)
plt.savefig("D:\DATACAMP\intro_to_Python\plots/stupid_result_plot.png")

plt.figure()
plt.title("Alif you stupid dump ass. look what you did_scatter_plot")
plt.scatter(semester,cgpa)
plt.savefig("D:\DATACAMP\intro_to_Python\plots/stupid_result_scatter.png")
plt.show()