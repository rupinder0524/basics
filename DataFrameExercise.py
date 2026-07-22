# # Exercise-1


# import pandas as pd
# df_csv=pd.read_csv("students.csv")
# print(df_csv)
# print("Top 5 players by run:")
# top=df_csv.sort_values(by="Runs",ascending=False)
# print(top)
# print()
# print("Players with strike rate >140")
# max_strike_Rate=df_csv[df_csv["Strike Rate"]>140]
# print(max_strike_Rate)
# print()
# print("Average Run scored by players: ")
# average_run=df_csv["Runs"].mean()
# print(average_run)
# print()
# print("Player With Maximum Runs: ")
# max_runs = df_csv["Runs"].max()
# player=df_csv[df_csv["Runs"]==max_runs]
# print(max_runs)
# print()
# print(player)
# print()

# import matplotlib.pyplot as plt
# # plt.bar(df_csv["Player Name"],df_csv["Runs"],color="Red")
# # plt.xlabel("Runs")
# # plt.ylabel("Players Name")
# # plt.title("Runs Scored By Players")
# # plt.show()

# # plt.scatter(df_csv["Matches"],df_csv["Runs"],color="skyblue")
# # plt.xlabel("Matches")
# # plt.ylabel("Runs")
# # plt.title("MAtTCHES v/s RUNS")
# # plt.grid(True)
# # plt.show()


# plt.hist(df_csv["Strike Rate"],color="green")
# plt.xlabel("value")
# plt.ylabel("Frequency")
# plt.title("Strike rate Distribution")
# plt.grid(True)
# plt.show()


 # Exercise-2

# import pandas as pd
# data={
#     "flight number":[101,102,103,104,105],
#     "Source":["Delhi","Ludhiana","Mohali","Kolkatta","Mumbai"],
#     "Destination":["London","USA","UK","Finland","Australia"],
#     "Ticket Price":[1000,200000,150000,120000,30000],
#     "Seats Available":[25,20,14,26,11]
#     }
# df=pd.DataFrame(data)
# print("Flight Costing more than 7000: ")
# cost=df[df["Ticket Price"]>7000]
# print(cost)
# print()
# print("Left seats: ")
# seats=df[df["Seats Available"]<25]
# print(seats)
# print()
# print("Highest Ticket Price: ")
# Max_price=df["Ticket Price"].max()
# print(Max_price)
# print()
# print("Lowest Ticket Price: ")
# Min_Price=df["Ticket Price"].min()
# print(Min_Price)
# print()
# print("Average Ticket Price: ")
# average=df["Ticket Price"].mean()
# print(average)
# print()

# import matplotlib.pyplot as plt
# destination=df["Destination"]
# plt.pie([1, 1, 1, 1, 1],labels=destination,autopct="%1.1f%%")
# plt.title("Destination Distribution")
# plt.show()


# plt.bar(df["flight number"],df["Ticket Price"],color="red",width=0.6)
# plt.xlabel("Flight Number")
# plt.ylabel("Ticket Price")
# plt.title("Ticket Price Bar Chart")
# plt.show()


# exercise-3
import pandas as pd
df_csv = pd.read_csv("SmartPhoneMaeketAnalysis.csv")
print(df_csv)
print("phone with RAM>=8GB")
Phone_RAM=df_csv[df_csv["RAM"]>=8]
print(Phone_RAM)
print()
print("Phone price more than 3000")
phone_Price=df_csv[df_csv["Price"]<30000]
print(phone_Price)
print()
print("Highest Battery Capacity")
high_battery=df_csv["Battery"].max()
battery=df_csv[df_csv["Battery"]==high_battery]
print(high_battery)
print(battery)
print()
print("Average Price")
average=df_csv["Price"].mean()
print(average)
print()

import matplotlib.pyplot as plt
plt.scatter(df_csv["RAM"],df_csv["Price"],color="Red")
plt.xlabel("RAM")
plt.ylabel("Price")
plt.grid(True)
plt.title("RAm v/s Price")
plt.show()

plt.hist(df_csv["Battery"],color="green")
plt.xlabel("value")
plt.ylabel("Frequency")
plt.title("Battery Capacity")
plt.grid(True)
plt.show()

plt.bar(df_csv["Brand"],df_csv["Price"],color="Red")
plt.xlabel("Brand")
plt.ylabel("Price")
plt.grid(True)
plt.title("Brand v/s Price")
plt.show()