# TECOB220
# Yash Morankar

import csv
import matplotlib.pyplot as plt

#============== Write data into csv =================
# for Bar Plot
heading = ["Country_Name","GOLD MEDALS","SILVER MEDALS","BRONZE MEDALS"]
entry1 = ["Aus",120,60,30]
entry2 = ["Ind",110,70,40]
entry3 = ["Eng",90,60,50]

data = [heading, entry1, entry2, entry3]

with open("Game_medal.csv",'w') as f:
    writer = csv.writer(f,lineterminator="\n")
    writer.writerows(data)

#============== Plotting Graph =================
# Bar Chart
Country = []
value1 = []
value2 = []
value3 = []

with open("Game_medal.csv",'r') as f:
    reader = csv.reader(f)
    heading = next(reader)
    for row in reader:
        Country.append(list(row)[0])
        value1.append(int(list(row)[1]))
        value2.append(int(list(row)[2]))
        value3.append(int(list(row)[3]))

xAxis1 = [i - 0.2 for i, _ in enumerate(Country)]
xAxis2 = [i for i, _ in enumerate(Country)]
xAxis3 = [i + 0.2 for i, _ in enumerate(Country)]

plt.bar(xAxis1, value1, width=0.2, color='skyblue')
plt.bar(xAxis2, value2, width=0.2, color='orange')
plt.bar(xAxis3, value3, width=0.2, color='green')

plt.title('Olympics 2018', fontsize=16, color='magenta')
plt.xlabel('Nations', fontsize=14, color='cyan')
plt.ylabel('Medals', fontsize=14, color='cyan')
plt.xticks([i for i, _ in enumerate(Country)], Country)
plt.legend(heading[1:], loc ="upper right")

plt.show()