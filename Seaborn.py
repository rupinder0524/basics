# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# # import seaborn as sns
# df=pd.read_csv("AirportTraffic.csv")
# print(df)
# print()
# print("Using Head")
# print(df.head())
# print()
# print("Using Tail")
# print(df.tail())
# print()
# print("Using Info")
# print(df.info())
# print()
# print("Using Describe")
# print(df.describe())
# print()
# print("Handle Missing Values")
# print(df["Ticket_Price"].fillna(df["Ticket_Price"].mean()))
# print(df["Flight_Duration"].fillna(df["Flight_Duration"].mean()))
# print()
# print("Number of Duplicate Rows")
# print(df.duplicated().sum())
# print()


# sns.scatterplot(data=df,
#                 x="Ticket_Price",
#                 y="Flight_Duration",
#                 hue="Travel_Class"
#                 )
# plt.title("Ticket Price vs Flight Duration")
# plt.show()

# line = df.groupby("Airline")["Ticket_Price"].mean()
# sns.lineplot(
#     data=df,
#     x="Airline",
#     y="Ticket_Price"
# )
# plt.title("Average Ticket Price by airline")
# plt.show()


# line1=df.groupby("Airline")["Delay_Minutes"].mean()
# sns.barplot(
#     data=df,
#     x="Airline",
#     y="Delay_Minutes",
# )
# plt.title("Average delay by Airline")
# plt.show()


# sns.boxplot(
#     data=df,
#     x="Travel_Class",
#     y="Delay_Minutes"
# )
# plt.title("Delay Distribution by Travel Class")
# plt.show()

# sns.histplot(
#     data=df,
#     x="Ticket_Price",
#     bins=30
#  )
# plt.title("Ticket Price")
# plt.show()


# print()
# print("Highest Average TicKet Price")
# print(df.groupby("Airline")["Ticket_Price"].mean().max())

# print()
# print("Travel class with lowest delay")
# print(df.groupby("Travel_Class")["Delay_Minutes"].mean().min())

# print()
# top_destination = (
#     df["Destination_City"].value_counts())
# print(top_destination)

# print("Airline Management Insights")
# print("1. Premium travel classes generate significantly higher ticket revenue.")
# print("2. Economy class experiences the highest average delays and needs operational improvements.")
# print("3. Airlines with premium pricing should focus on maintaining high service quality.")
# print("4. High-demand destination cities may require additional flight frequency.")
# print("5. Longer flights generally have higher ticket prices, supporting distance-based pricing.")


# Exercise-2

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# df=pd.read_csv("EV_Charging.csv")
# print(df)
# print()

# print("Handle Missing Values")
# print(df["Cost"].fillna(df["Cost"].mean()))
# print(df["Energy_Consumed"].fillna(df["Energy_Consumed"].mean()))
# print()

# print("Using Head")
# print(df.head())
# print()
# print("Using Tail")
# print(df.tail())
# print()
# print("Using Info")
# print(df.info())
# print()
# print("Using Describe")
# print(df.describe())
# print()
# sns.scatterplot(data=df,
#                 x="Charging_Time",
#                 y="Energy_Consumed",
#                 hue="Charging_Type"
#                 )
# plt.title("Charging_Time v/s Energy_Consumed")
# plt.show()

# line = df.groupby("City")["Energy_Consumed"].mean()
# sns.lineplot(
#     data=df,
#     x="City",
#     y="Energy_Consumed"
# )
# plt.title("Average Energy Consumed by city")
# plt.show()


# line1=df.groupby("City")["Cost"].sum()
# sns.barplot(
#     data=df,
#     x="City",
#     y="Cost",
# )
# plt.title("Total revenue by city")
# plt.show()


# sns.boxplot(
#     data=df,
#     x="Charging_Type",
#     y="Cost"
# )
# plt.title("cost Distribution by charging_Type ")
# plt.show()

# sns.histplot(
#     data=df,
#     x="Charging_Time",
#     bins=30
#  )
# plt.title("Ticket Price")
# plt.show()

# print("City Generating Maximum Revenue")
# print(df.groupby("City")["Cost"].max().head(1))
# print()
# print("Average Charging Time Bt vechicle type")
# print(df.groupby("Vehicle_Type")["Charging_Time"].mean())
# print()

#  exercise-3


# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# df=pd.read_csv("Farm_Data.csv")
# print(df)
# print()

# print("Handle Missing Values")
# print(df["Yield "].fillna(df["Yield "].mean()))
# print(df["Temperature "].fillna(df["Temperature "].mean()))
# print()

# print("Using Head")
# print(df.head())
# print()
# print("Using Tail")
# print(df.tail())
# print()
# print("Using Info")
# print(df.info())
# print()
# print("Using Describe")
# print(df.describe())
# print()

# sns.scatterplot(
#                 data=df,
#                 x="Rainfall",
#                 y="Yield",
#                 hue="Crop"
#                 )
# plt.title("Rainfall vs Yield")
# plt.show()

# line = df.groupby("State")[" Yield "].mean()
# sns.lineplot(
#     data=line,
#     x="State",
#     y="Yield"
# )
# plt.title("Average Yield  by State")
# plt.show()

# sns.boxplot(
#     data=df,
#     x="Crop",
#     y="Yield"
# )
# plt.title("Yield Distribution by Crop ")
# plt.show()

# sns.histplot(
#     data=df,
#     x="Rainfall",
#     bins=30
#  )
# plt.title("Ticket Price")
# plt.show()

# print("Which crop gives the highest yield?")
# print(df.groupby("Crop")["Yield "].max().head(1))
# print()
# print("Which state has the highest average production?")
# print(df.groupby("State")["Yield "].mean().idxmax())
# print()


# print("Five Recommendation of farmers")
# print("Grow crop varieties that consistently produce higher yields in your region.")
# print("Use fertilizers according to soil test recommendations rather than applying excessive amounts")
# print("Monitor rainfall forecasts and supplement with irrigation when rainfall is insufficient.")
# print("Select crops suited to local temperature and climate conditions.")
# print("Use farm data and weather analytics to make informed decisions on planting, irrigation, and fertilizer application.")


# # Exercise-5
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# import seaborn as sns
df=pd.read_csv("space_mission.csv")
print(df)
print()
print("Using Head")
print(df.head())
print()
print("Using Tail")
print(df.tail())
print()
print("Using Info")
print(df.info())
print()
print("Using Describe")
print(df.describe())
print()
print("Handle Missing Values")
print(df["Mission_Cost"].fillna(df["Mission_Cost"].mean()))
print(df["Payload_Weight"].fillna(df["Payload_Weight"].mean()))
print()
print("Number of Duplicate Rows")
print(df.duplicated().sum())
print()


sns.scatterplot(data=df,
                x="Mission_Cost",
                y="Payload_Weight",
                hue="Success"
                )
plt.title("Mission_Cost v/s payload_Weight")
plt.show()



line1=df.groupby("Country")["Mission_Cost"].mean()
sns.barplot(
    data=df,
    x="Country",
    y="Mission_Cost",
)
plt.title(" Mission_Cost by Country")
plt.show()


sns.boxplot(
    data=df,
    x="Rocket_Type",
    y="Payload_Weight"
)
plt.title("payload Distribution by Rocket type")
plt.show()

sns.histplot(
    data=df,
    x="Mission_Cost",
    bins=5
 )
plt.title("Mission Cost")
plt.show()


print()
print("Which country has highest average mission cost?")
print(df.groupby("Country")["Mission_Cost"].mean().idxmax())

# print()
print("Which rocket type carries the heaviest payload?")
print(df.groupby("Rocket_Type")["Payload_Weight"].mean().idxmax())
# print(a)

print()
print("What is the mission success rate for each country?")
success = df.groupby("Country")["Success"].value_counts()
print(success)

print()
print("Five Recommendations")
print()
print("1. Invest more in rocket types that consistently carry heavier payloads.")
print("2. Study the practices of countries with the highest mission success rates.")
print("3. Optimize mission costs by improving launch efficiency and resource planning.")
print("4. Perform regular maintenance and testing to reduce mission failures.")
print("5. Increase collaboration and technology sharing to improve mission success and reduce costs.")