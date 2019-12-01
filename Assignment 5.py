# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 14:54:43 2019

@author: Satya Manepalli
"""

import pandas as pd
#file is read using read_excel function
df = pd.read_excel('C:/DataScience/In Class/Travel_TripAdvisor_v1/Data_TripAdvisor_v1.xls')
print (df)
print ("----------------------------------------------------------------------------------------")
print ("******Number of Hotels Rated*******")
print ("----------------------------------------------------------------------------------------")
#Number of Hotels Rated is found using nunique() on ID_HOTEL
print(df['ID_HOTEL'].nunique())
print ("----------------------------------------------------------------------------------------")
print ("******List of All the Hotels*******")
print ("----------------------------------------------------------------------------------------")
#list of All The Hotels is found using unique() on ID_HOTEL
List_Of_Unique_Hotels = df['ID_HOTEL'].unique()
print (List_Of_Unique_Hotels)
print ("----------------------------------------------------------------------------------------")
print ("******Average Rating of Each Hotel*******")
print ("----------------------------------------------------------------------------------------")
#Group by applied for Unique Hotel_ID for each hotel
Mean_Rated = df.groupby(['ID_HOTEL'])[['Rating']].mean()
#Average Rating of each the Hotels
print (Mean_Rated)

#Highest Rated Hotel in Each Time Zone
print ("----------------------------------------------------------------------------------------")
print ("******Highest Rated Hotels in Each Time Zone*******")
print ("----------------------------------------------------------------------------------------")
#a function written to check the rating of each hotel woith respect to each time zone and returning the highest rated hotel
def func(Hotel):
    return Hotel[Hotel['Rating'] == Hotel['Rating'].max()]
#Groupby is applied on User_TIMEZONE to find retrieve the Hightest rating
#Highest_Rated_Hotel = df.groupby(['USER_TIMEZONE'], as_index=False)[['ID_HOTEL','Rating']].max()
#print (Highest_Rated_Hotel)
Highest_Rated_Hotel = df.groupby(['USER_TIMEZONE'], as_index=False).apply(func)
#print (Highest_Rated_Hotel)   

#Highest Rated Hotel in Each and Every City with its Rating retrieved by applying groupby on hotel_city and by applying max() on rat
Highest_Rated_Hotel_In_City = df.groupby(['HOTEL_CITY'], as_index=False)[['ID_HOTEL','Rating']].max()
print ("----------------------------------------------------------------------------------------")
print ("******Extra Question*******")
print ("******Highest Rated Hotel in Each and Every City with its Rating*******")
print ("----------------------------------------------------------------------------------------")
#print (Highest_Rated_Hotel_In_City)
#Highest Rated Hotels in Seattle with Rating
print ("----------------------------------------------------------------------------------------")
print ("******Highest Rated Hotel in Seattle with its Rating*******")
print ("----------------------------------------------------------------------------------------")
#finding the highest rated hotel in seattle using loc()
#print (Highest_Rated_Hotel_In_City.loc[Highest_Rated_Hotel_In_City['HOTEL_CITY'] == 'Seattle'])

#Unique_USER_ID = df['ID_USER'].unique()
#print (Unique_USER_ID)

print ("----------------------------------------------------------------------------------------")
print ("******Extra Question*******")
print ("******States With Number of its Users*******")
print ("----------------------------------------------------------------------------------------")
#groupby on user state to find number of users and count of them
State_With_More_Users = df.groupby(['USER_STATE',], as_index=False)[['ID_USER']].count()
#print (State_With_More_Users)
print ("----------------------------------------------------------------------------------------")
print ("******States With Highest Number of its Users*******")
print ("----------------------------------------------------------------------------------------")
#idxmax on id user to find max value of users 
print (State_With_More_Users.loc[State_With_More_Users['ID_USER'].idxmax()])


print ("----------------------------------------------------------------------------------------")
print ("******Extra Question*******")
print ("******All Time Zones with Average Rating for Hotels*******")
print ("----------------------------------------------------------------------------------------")
#group by on user_timezone and max() on rating to find higjhest rated user_timezone
Highest_Rating_For_TimeZone = df.groupby(['USER_TIMEZONE'], as_index=False)[['Rating']].mean()
#Average Rating of each the Hotels
print (Highest_Rating_For_TimeZone)
print ("----------------------------------------------------------------------------------------")
print ("******Time Zone with Highest Average Rating for Hotels*******")
print ("----------------------------------------------------------------------------------------")
#idxmax on rating for the above data
print (Highest_Rating_For_TimeZone.loc[Highest_Rating_For_TimeZone['Rating'].idxmax()])


#print(df.ID_HOTEL.unique())

#Hotels_Rated = df.groupby(['ID_HOTEL'])['ID_HOTEL'].count()
#Sum of total number of Hotels Rated
#print (Hotels_Rated.sum())



#print("\nRead file with read_table:")
#df1= pd.read_table('C:/DataScience/In Class/Travel_TripAdvisor_v1/Data_TripAdvisor_v1.xls',sep=',')
#print(df1)
#print (df.sort_values('Rating'))
