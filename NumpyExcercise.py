# # Exercise 1 

# import numpy as np
# arr=np.array([10,50,84,12,13,54,62,25,0,11])
# print("scores: ",arr)
# print("Highest score: ",np.max(arr))
# print("Lowest Score: ",np.min(arr))
# print("Average Score: ",np.mean(arr))
# print("Total Score: ",np.sum(arr))


# Exercise 2

# import numpy as np
# arr=np.arange(1,101,1)
# print("All Seat numbers: \n")
# print(arr)
# reshaped=arr.reshape(10,10)
# print("After Reshaping array : ",reshaped)
# print("First Row: ",reshaped[0])
# print("Last Row:",reshaped[-1])


# Exercise 3

# import pandas as pd
# s= pd.Series([57.9 ,108.9 ,14906,227.9 ,778.6 ],index=(["Mercury","venus","Earth","Mars","Jupiter"]))
# print("Complete Series: ")
# print(s)
# print( )
# print("Earth Distance: ")
# print(s["Earth"])
# print( )
# print("First Three Planets:")
# print(s[ :3])


# Exercise 4

# Water_Intake=[7,6,5,8,7,5,4]
# with open("water_log.txt","w")as file:
#     for intake in Water_Intake:
#         file.write(str(intake)+"\n")
# with open ("water_log.txt","r") as file:
#     for line in file:
#         print("daily water intake: ",line)

# Exercise 5

# import numpy as np
# arr = np.arange(1,37,1)
# reshaped=arr.reshape(6,6)
# print(reshaped)
# print("Shape of the Array is : ",reshaped.shape)
# print("Size of Array is: ",reshaped.size)
# print("Dimension of the Array is: ",reshaped.ndim)


# Exercise 6

# import numpy as np
# phone_price=np.array([30000,78000,25000,54000,150000,10000,8000,65000,98000,10000,55000,30000])
# print("Most Expensive Phpne: ",np.max(phone_price))
# print("Average pricee : ",np.mean(phone_price))
# print("stamdard deviation : ",np.std(phone_price))
# print("Phones costing more than ₹30,000:")
# print(phone_price[phone_price > 30000])


# Exercise 7

# import numpy as np
# book_id = np.arange(1001,1101,1)
# reshaped=book_id.reshape(10,10)
# print(reshaped)
# print ("Alternative Rows: ")
# print(reshaped[: : 2])
# print ("Alternative Columns: ")
# print(reshaped[:,: : 2])
# print("Flatten Matrix: ")
# flattened=reshaped.flatten()
# print(flattened)


# Exercise 8

# import numpy as np
# beds = np.array([True, False, True, True, False, False, True, False, True, True])
# OccupiedBeds=np.sum(beds)
# print("Number of Occupied beds: ",OccupiedBeds)
# VacantBeds=np.sum(~beds)
# print("Number of Vacant Beds",VacantBeds)
# print("vacant beds :",beds[beds==False])

# Exercise 9

# import pandas as pd
# rating = pd.Series(
#     [5,2,8,9,10,4,6,3,5,1],index=["Python", "Java", "Data Science", "Web Development","C++", "Machine Learning", "SQL", "AI","Cloud Computing", "Cyber Security"])
# print("Maximum Rating Course:", rating.max())
# print("Lowest Rating Course:", rating.min())
# print("Average Rating Course:", rating.mean())
# print("Courses with Rating greater than 4:", rating[rating > 4])


# Exercise 10 

# import csv
# import numpy as np
# with open ("Electricity_Consumption.csv","w")as file:
#     writer=csv.writer(file)
#     writer.writerow(["HouseNo","UnitsConsumed"])
#     writer.writerow([15124,115])
#     writer.writerow([15125,225])
#     writer.writerow([10345,350])
#     writer.writerow([10422,200])
#     writer.writerow([10574,300])
# units=[]
# with open ("Electricity_Consumption.csv","r")as file:
#     reader=csv.reader(file)
#     next(reader)
    
#     for row in reader:
#        units.append(int(row[1]))
# units=np.array(units)
# print("Total Units: ",np.sum(units))
# print("Average Units: ",np.mean(units))
# print("Maximum Units: ",np.max(units))
# print("Minimum Units:",np.min(units))



# Exercise 11

# import numpy as np
# days=np.array(["Sunday","Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday"])
# Passengers=np.array([120,130,122,124,200,204,101])
# print("Total number of Passengers : ",np.sum(Passengers))
# busiest=np.argmax(Passengers)
# print("Busiest Day",days[busiest])
# least=np.argmin(Passengers)
# print("Least Day: ",days[least])
# average=np.mean(Passengers)
# print("days with Passengers above average: ",days[Passengers>average])

# Exercise 12

# import numpy as np
# StepCount=np.array([1000,1500,15001,1478,2564,600,500,700,800,745,3071,578,1236,1400,1555,17892,12361,1236,1452,1478,14569,145,147,9874,1557,6547,24789,2252,2222,1111,6647,5542,5778,2000])
# print("Maximum Number of steps: ",np.max(StepCount))
# print("average Steps: ",np.mean(StepCount))
# print("Median",np.median(StepCount))
# print("Standard deviation",np.std(StepCount))
# print("Days with more than 10,000 steps:")
# for i in range(len(StepCount)):
#     if StepCount[i] > 10000:
#         print("Day", i + 1, ":", StepCount[i], "steps")


# Exercise 13

# import numpy as np
# RoomPrice=np.array([[100,200,300,400,500,600],
#                     [700,800,900,1000,1100,1200],
#                     [1300,1400,1500,1600,1700,1800],
#                     [1900,2000,2100,2200,2300,2400],
#                     [2500,2600,2700,2800,2900,3000]])
# print("Total Revenue: ",np.sum(RoomPrice))
# print("Cheapest Room: ",np.min(RoomPrice))
# print("Most Expensive Room: ",np.max(RoomPrice))

# Revenue_per_floor=np.sum(RoomPrice,axis=1)
# print("revenue per floor(in Rows):",Revenue_per_floor)

# RevenuePerFloor=np.sum(RoomPrice,axis=0)
# print("Revenue Per Floor(in columns): ",RevenuePerFloor)


# Exercise 14

# import numpy as np
# temperature=np.array ([25,20,35,19,45,
#                       21,22,32,18,24,
#                       25,26,35,34,37])
# days=np.arange(1,16)
# print("Days above 35°C: ",days[temperature>35])
# print("Days below 20°C: ",days[temperature<20])
# print("Temperatures between 25°C and 30°C",temperature[(temperature >= 25) & (temperature <= 30)])

# Exercise 16

# import numpy as np
# RunsScored=np.array([122,111,145,167,146,
#                      200,126,148,144,213,
#                      200,178,199,121,])

# RunsConceded = np.array([170,200,150,210,165,
#                         215,180,140,190,185, 
#                         160,230,175,195])

# matches=np.arange(1,15)

# print("Highest Score: ",np.max(RunsScored))
# print("Lowest Score: ",np.min(RunsScored))

# difference=RunsScored- RunsConceded
# print("Difference:",difference)
# Average=np.average(RunsScored)
# print(" Matches where team scored above average: ",matches[RunsScored>Average])

# Exercise 17

# AQI = np.array([
#     85,120,95,160,210,
#     180,75,60,145,190,
#     220,250,130,110,90,
#     40,55,100,175,200,
#     230,150,125,80,65,
#     140,185,240,105,95
# ])
# days=np.arange(1,31)
# good=AQI[AQI<50]
# print("Good AQI: ",good)
# print("Good AQI Days:",days[AQI<50])
# moderate=AQI[(AQI>50)&(AQI<100)]
# print("Moderate AQI: ",moderate)
# print("Moderate AQI Days:",days[(AQI>50)&(AQI<100)])
# poor=AQI[AQI>100]
# print("Poor AQI:",poor)
# print("Poor AQI Days:",days[AQI>100])


# Exercise 18

# import numpy as np
# English_Marks=np.array([14,25,54,87,56,98,74,25,25,57,
#                        45,25,87,9,87,36,54,58,44,11,
#                        14,25,74,88,88,22,14,34,47,78,
#                        24,66,64,23,22,00,14,10,20,57,
#                        25,78,99,54,25,36,74,47,78,55])
# student=np.arange(1,51)
# Average=np.average(English_Marks)
# print("Class average: ",Average)
# print("Standard Deviation: ",np.std(English_Marks))
# print("Students above Average:",student[English_Marks>Average])
# print("Students below Average:",student[English_Marks<Average])

# Exercise 20
# import numpy as np
# temperature = np.array([
#     22.5, 23.2, 21.8, 20.6, 19.4, 18.7,
#     17.9, 18.3, 21.5, 25.2, 28.6, 30.1,
#     32.4, 33.7, 34.5, 35.8, 33.9, 31.6,
#     29.8, 27.4, 26.2, 25.6, 24.3, 23.1
# ])
# print("Maximum Temperature:",np.max(temperature))
# print()
# print("Minimum Temperature:",np.min(temperature))
# print()
# reshaped=temperature.reshape((6,4))
# print()
# print("After reshaping of Array")
# print(reshaped)
# print("Average Temperature (in rows):",np.mean(reshaped,axis=0))
# print()
# print("Average Temperature (in Columns):",np.mean(reshaped,axis=1))
# print()
# flattned=reshaped.flatten()
# print(flattned,flattned.shape)
# print()
# print("After round off:\n",np.round(temperature))
# print()
# print("All unique values:\n",np.unique(temperature))


# Exercise 19

# import csv
# import numpy as np
# with open("SalesReport.csv","w")as file:
#     writer = csv.writer(file)
#     writer.writerow(["Date", "Petrol Sold", "Diesel Sold"])
#     writer.writerow(["01-01-2025", 500, 300])
#     writer.writerow(["02-01-2025", 700, 400])
#     writer.writerow(["03-01-2025", 600, 350])
# date=[]
# petrol=[]
# diseal=[]
# with open("SalesReport.csv","r")as file:
#     reader=csv.reader(file)
#     next(reader)
#     for row in reader:
#         if len(row) == 0:
#             continue    
#         date.append(row[0])
#         petrol.append(int(row[1]))
#         diseal.append(int(row[2]))
# petrol = np.array(petrol)
# diseal = np.array(diseal)
# print("Total Petrol Sold: ",np.sum(petrol))
# print("Total Diseal Sold",np.sum(diseal))
# total_sales=petrol+diseal
# print("Highest Sales Day:", date[np.argmax(total_sales)])
# print("Lowest Sales Day:", date[np.argmin(total_sales)])
# print("Average Daily Sales:", np.mean(total_sales))

# import csv
# with open("Sales_Report.csv","w",newline="")as file:
#     writer=csv.writer(file)
#     writer.writerow(["Date","Pertrol Sold","Diseal Sold"])
#     writer.writerow([21,1500,1600])
#     writer.writerow([14,1400,1700])
# with open("Sales_Report .csv","r")as file:
#     reader=csv.reader(file)

# import numpy as np
# print("Total Petrol Sold: ",np.sum)

# Olympic Medal Table
# Create a CSV:
# Columns:

# Country
# Gold
# Silver
# Bronze
# Read the file.
# Calculate:

# Total medals for each country.
# Country with maximum gold medals.
# Country with highest total medals.

import csv
import numpy as np
with open("Medal Record.csv","w",newline="")as file:
    writer=csv.writer(file)
    writer.writerow(["country","gold","silver","bronze"])
    writer.writerow(["India",20,14,12])
    writer.writerow(["Canada",24,15,30])
    writer.writerow(["USA",27,25,37])
gold=[]
medal=[]
country=[]
with open("Medal Record.csv","r")as file:
    reader=csv.reader(file)
    next(reader)
    for row in reader:
        gold.append(row[1])
        country.append(row[0])
        total=int(row[1])+int(row[2])+int(row[3])
        medal.append(total)
        print(row[0],"has",total,"medal")
gold=np.array(gold)
medal=np.array(medal)
index1=np.argmax(gold)
index2=np.argmax(medal)
print("Country with maximum gold medals: ",country[index1])
print("Country with highest total medals: ",country[index2])