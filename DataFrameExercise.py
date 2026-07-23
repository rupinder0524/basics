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
# destination=df["Destination"].value_counts()
# destination.plot(kind="pie",autopct="%1.1f%%")
# plt.title("Destination Distribution")
# plt.show()

# plt.bar(df["flight number"],df["Ticket Price"],color="red",width=0.6)
# plt.xlabel("Flight Number")
# plt.ylabel("Ticket Price")
# plt.title("Ticket Price Bar Chart")
# plt.show()


# exercise-3
# import pandas as pd
# df_csv = pd.read_csv("SmartPhoneMaeketAnalysis.csv")
# print(df_csv)
# print("phone with RAM>=8GB")
# Phone_RAM=df_csv[df_csv["RAM"]>=8]
# print(Phone_RAM)
# print()
# print("Phone price more than 3000")
# phone_Price=df_csv[df_csv["Price"]<30000]
# print(phone_Price)
# print()
# print("Highest Battery Capacity")
# high_battery=df_csv["Battery"].max()
# battery=df_csv[df_csv["Battery"]==high_battery]
# print(high_battery)
# print(battery)
# print()
# print("Average Price")
# average=df_csv["Price"].mean()
# print(average)
# print()

# import matplotlib.pyplot as plt
# plt.scatter(df_csv["RAM"],df_csv["Price"],color="Red")
# plt.xlabel("RAM")
# plt.ylabel("Price")
# plt.grid(True)
# plt.title("RAm v/s Price")
# plt.show()

# plt.hist(df_csv["Battery"],color="green")
# plt.xlabel("value")
# plt.ylabel("Frequency")
# plt.title("Battery Capacity")
# plt.grid(True)
# plt.show()

# plt.bar(df_csv["Brand"],df_csv["Price"],color="Red")
# plt.xlabel("Brand")
# plt.ylabel("Price")
# plt.grid(True)
# plt.title("Brand v/s Price")
# plt.show()


# exercise-4
# import pandas as pd
# data={
#     "City":["Mohali","Ludhiana","Fazilika","Chandigarh","Delhi"],
#     "Temperature":[35,40,41,20,45],
#     "Humidity":[80,85,81,82,83],
#     "Rainfall":[35,20,70,65,52]
# }
# df=pd.DataFrame(data)
# print("City Where Temperature greater than 35 degree")
# temp=df[df["Temperature"]>35]
# print(temp)
# print()
# print("City Where Humidity Greater than 70%")
# humidity=df[df["Humidity"]>70]
# print(humidity)
# print()
# print("Average Rainfall")
# average=df["Rainfall"].mean()
# print(average)
# print()

# import matplotlib.pyplot as plt
# plt.scatter(df["Temperature"],df["Humidity"],color="red")
# plt.xlabel("Temperature")
# plt.ylabel("Humidity")
# plt.title("Temperatute v/s Humidity")
# plt.grid(True)
# plt.show()

# plt.hist(df["Temperature"],edgecolor="black",color="blue",bins=5)
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.title("Temperature Histogram")
# plt.grid(axis='y',alpha=0.7)
# plt.show()

# plt.plot(df["Rainfall"],color="red",linestyle="--",linewidth=2)
# plt.xlabel("values")
# plt.ylabel("Frequency")
# plt.title("Rainfall Line Graph")
# plt.grid(True)
# plt.show()

# exercise-5

# import pandas as pd
# df=pd.read_csv("order.csv")
# df["Total"]=df["Price"]*df["Quantity"]
# print(df)
# print()
# print("Highest Order Value:")
# High_Order_value=df["Total"].max()
# print(High_Order_value)
# print()
# print("Lowest Order Value")
# Low_Order_value=df["Total"].min()
# print(Low_Order_value)
# print()
# print("Average Order Value:")
# average=df["Total"].mean()
# print(average)
# print()
# print("Order above 5000")
# Order=df[df["Total"]>5000]
# print(Order)
# print()

# import matplotlib.pyplot as plt
# plt.plot(df["Total"],color="red",linestyle="--",linewidth=2)
# plt.xlabel("Values")
# plt.ylabel("Frequency")
# plt.title("Line Graph of order value")
# plt.grid(True)
# plt.show()

# product=df["Product"].value_counts()
# product.plot(kind="pie",autopct="%1.1f%%")
# plt.title("Product Distribution")
# plt.show()


# exercise-6
# import pandas as pd
# data={
#     "movie":["Dangal","Bajrangi Bhaijaab","3 Idiots","PK","Shersaah"],
#     "genre":["Biography","Comedy,Drama","Drama","Comedy","Biography"],
#     "duration":["155min","153min","170min","135min","146min"],
#     "rating":[5,7,8,9,4],
#     "release year":[2016,2015,2026,2021,2018]
# }
# df=pd.DataFrame(data)
# print("Movie after 2020")
# Movie=df[df["release year"]>2020]
# print(Movie)
# print()
# print("Movies Whose Rating is Greater than 8: ")
# Rating=df[df["rating"]>8]
# print(Rating)
# print()
# print("Longest Movie")
# Longest_movie=df["duration"].max()
# print(Longest_movie)
# print()
# print("Shortest Movie")
# Shortest_movie=df["duration"].min()
# print(Shortest_movie)
# print()
# print("Average Movie")
# average=df["rating"].mean()
# print(average)
# print()

# import matplotlib.pyplot as plt
# Genre=df["genre"].value_counts()
# Genre.plot(kind="pie",autopct="%1.1f%%")
# plt.title("Genre Distribution")
# plt.show()



# plt.bar(df["movie"],df["rating"],color="red")
# plt.xlabel("Movie")
# plt.ylabel("Rating")
# plt.grid(True)
# plt.title("Rating Bar Graph")
# plt.show()


# plt.hist(df["rating"],color="red",edgecolor="black",linewidth=1.5,width=0.6)
# plt.xlabel("values")
# plt.ylabel("frequency")
# plt.title("Rating Histogram")
# plt.show()


# exercise-7
# import pandas as pd
# data={
#     "Member Name":["Nick","John","David","Lilly","Adam","Marian","ana","Sahid","Leo","orry"],
#     "Age":[21,45 ,23 ,33,26,65,25,45,44,41 ],
#     "Weight":["60 kg","70kg","75kg","100kg","92kg","44kg","66kg","55kg","41kg","30kg"],
#     "Membership Plan": ["Basic","Premium","Gold","Standard","Platinum","Gold","Standard","Platinum","Basic","Premium"],
#     "Monthly Fee": [1000,2000,3000,1500,4000,3000,1500,4000,1000,2000,]
#     }
# df=pd.DataFrame(data)
# print("Member above 30 years:")
# member=df[df["Age"]>30]
# print(member)
# print()
# print("Premium members Only")
# Members=df[df["Membership Plan"]=="Premium"]
# print(Members)
# print()
# print("Average fee: ")
# average=df["Monthly Fee"].mean()
# print(average)
# print()

# import matplotlib.pyplot as plt
# plt.scatter(df["Age"],df["Weight"],color="Red")
# plt.xlabel("Age")
# plt.ylabel("Weight")
# plt.title("Scatter Chart")
# plt.grid(True)
# plt.show()


# plt.bar(df["Member Name"],df["Monthly Fee"],color="Red")
# plt.xlabel("x axis")
# plt.ylabel("y axis")
# plt.title("Bar chart")
# plt.grid(True)
# plt.show()

# membership_plan=df["Membership Plan"].value_counts()
# membership_plan.plot(kind="pie",autopct="%1.1f%%")
# plt.title("Pie chart")
# plt.show()


# Exercise-8
# import pandas as pd
# df = pd.read_csv("university.csv")
# print(df)
# print()
# print("Students that score marks above 80%")
# marks = df[df["Percentage"] > 80]
# print(marks)
# print()
# print("Students From Delhi")
# city=df[df["City"]=="Delhi"]
# print(city)
# print()
# print("Average percentage")
# average=df["Percentage"].mean()
# print(average)
# print()
# print("Number of student per course")
# count=df["Course"].value_counts()
# print(count)

# import matplotlib.pyplot as plt
# Payment=df["Course"].value_counts()
# Payment.plot(kind="pie",autopct="%1.1f%%")
# plt.xlabel("x axis")
# plt.ylabel("y axis")
# plt.title("course Distribution")
# plt.show()

# plt.bar(df["Student_Name"],df["Percentage"],color="red")
# plt.xlabel("student name")
# plt.ylabel("percentage")
# plt.title("Percentage bar graph")
# plt.grid(True)
# plt.show()


# Exercise-9
# import pandas as pd
# df=pd.read_csv("RestaurantSales.csv")
# df["Total"]=df["Price"]*df["Quantity"]
# print(df)
# print()
# print("Total Revenue")
# Total_Revenue=df["Total"].sum()
# print(Total_Revenue)
# print()
# print("Most Ordered item")
# order=df["Quantity"].max()
# print()
# print("Highest Bill")
# Max_Bill=df["Total"].max()
# print(Max_Bill)
# print()
# print("Lowest Bill")
# Min_Bill=df["Total"].min()
# print(Min_Bill)
# print()
# print("Average Bill")
# average=df["Total"].mean()
# print(average)

# import matplotlib.pyplot as plt
# plt.bar(df["Food Item"],df["Quantity"],color="red")
# plt.xlabel("Food Items")
# plt.ylabel("Quatity")
# plt.title("Food Sales")
# plt.grid(True)
# plt.show()

# plt.hist(df["Total"], bins=5)
# plt.title("Bill Distribution")
# plt.grid(True)
# plt.show()

# Payment=df["Payment Mode"].value_counts()
# Payment.plot(kind="pie",autopct="%1.1f%%")
# plt.xlabel("x axis")
# plt.ylabel("y axis")
# plt.title("pie chart")
# plt.show()

# Exercise-10

# import pandas as pd
# data = {
#     "Country": ["India", "USA", "Canada", None, "Japan"],
#     "Population": [1428, 339, None, 27, 124],
#     "Literacy Rate": [77, 99, 99, None, 99],
#     "GDP": [3.7, 27.0, 2.1, 1.7, None],
#     "Continent": ["Asia", "North America", None, "Australia", "Asia"]
# }
# df = pd.DataFrame(data)
# print(df)
# df=pd.DataFrame(data)
# print("Country with population greater than 100 million")
# population=df[df["Population"]>100]
# print(population)
# print()
# print("Country with literacy rate greater than 90%")
# literacy=df[df["Literacy Rate"]>90]
# print(literacy)
# print()
# print("Highest GDP")
# High_GDP=df["GDP"].max()
# Highest= df[df["GDP"] == High_GDP]
# print(Highest)
# print()
# print("Lowest GDP")
# Lowest_GDP=df["GDP"].min()
# lowest = df[df["GDP"] == Lowest_GDP]
# print(lowest)
# print()
# print("Missing Values after fillna()")
# df["Literacy Rate"] = df["Literacy Rate"].fillna(df["Literacy Rate"].mean())
# df["GDP"] = df["GDP"].fillna(df["GDP"].mean())
# df["Continent"] = df["Continent"].fillna("Unknown")
# df["Country"] = df["Country"].fillna("Unknown")
# print(df)
# print()
# df.to_csv("World_Population_Cleaned.csv")


# import matplotlib.pyplot as plt
# plt.bar(df["Country"],df["GDP"],color="red")
# plt.xlabel("Country Name")
# plt.ylabel("Country GDP")
# plt.title("Bar Chart")
# plt.show()


# continent_distribution=df["Continent"].value_counts()
# continent_distribution.plot(kind="pie",autopct="%1.1f%%")
# plt.title("Continent Distribution")
# plt.show()

# plt.scatter(df["Population"],df["GDP"],color="red")
# plt.xlabel("Popution")
# plt.ylabel(" GDP")
# plt.title("Scatter plot ")
# plt.grid(True)
# plt.show()

# plt.hist(df["Literacy Rate"],color="red",edgecolor="black",linewidth=1.5,width=0.6)
# plt.xlabel("values")
# plt.ylabel("frequency")
# plt.title("Literacy Rate Histogram")
# plt.grid(True)
# plt.show()
