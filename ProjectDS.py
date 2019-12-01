# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 21:43:00 2019

@author: Satya Manepalli
"""
#In statistics, exploratory data analysis (EDA) is an approach to analyzing data sets 
#to summarize their main characteristics, often with visual methods. 
#A statistical model can be used or not, but primarily EDA is for seeing what the data can tell us beyond the formal modeling or hypothesis testing task.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import  Image
from IPython import get_ipython
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.svm import SVC


# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

import os
print(os.listdir("./"))

import warnings
warnings.filterwarnings("ignore")
get_ipython().run_line_magic('matplotlib', 'inline')

plt.figure(figsize=(15,10))
img = np.array(Image.open(r"C:\DataScience\In Class\IMG_20180818_140357.jpg"))
plt.imshow(img,interpolation="bicubic")
plt.axis("off")
plt.show()
#Reading the data from the files by using read_csv function
df_matches  = pd.read_csv('C:/DataScience/In Class/fifa-world-cup/WorldCupMatches.csv')
df_players  = pd.read_csv('C:/DataScience/In Class/fifa-world-cup/WorldCupPlayers.csv')
df_WorldCups  = pd.read_csv('C:/DataScience/In Class/fifa-world-cup/WorldCups.csv')
#Displaying data of matches file
print("MATCHES")
print(df_matches.head(3))
#Displaying data of players file
print("PLAYERS")
print(df_players.head(3))
#Displaying data of worldcups file
print("WORLD CUPS")
print(df_WorldCups.head(3))
print("================================================")
print ("Team with highest number of worldcup victories")
print("================================================")

#print (df_WorldCups)
#grouping by with winner and applying count function and finding out max value
print (df_WorldCups['Winner'].value_counts().idxmax())
fig, ax = plt.subplots()
df_WorldCups['Winner'].value_counts().plot(ax=ax, kind='bar')


#print("================================================")
#print ("City with maximum worldcup matches")
#print("================================================")

City_Max = df_matches["City"].value_counts().reset_index()
plt.figure(figsize=(8,8))
ax = sns.barplot(y = City_Max["index"][:15], x = City_Max["City"][:15], linewidth=1,edgecolor="k"*15)
plt.xlabel("Count of the Matches")
plt.ylabel("City")
plt.title("Cities which hosted for most number of worldcup victories",color='r')

#to numerate the bars in the histogram enumerate is used
#sliced the title of the city for needed
for i,j in enumerate("Matches  :" + City_Max["City"][:15].astype(str)):
    ax.text(.10,i,j,fontsize = 13,color="b")
plt.show()

print("================================================")
print ("Team with maximum worldcup victories")
print("================================================")

df_WinnerCount = df_WorldCups["Winner"].value_counts().reset_index()
df_WinnerCount.columns = ["Country","Count"]
df_WinnerCount["type"] = "WINNER"

df_RunnerCount = df_WorldCups["Runners-Up"].value_counts().reset_index()
df_RunnerCount.columns = ["Country","Count"]
df_RunnerCount["type"] = "RUNNER UP"

df_WinnerAndRunnerCount = pd.concat([df_WinnerCount,df_RunnerCount],axis=0)
#print(df_WinnerAndRunnerCount)

plt.figure(figsize=(8,10))
sns.barplot("Count","Country",data=df_WinnerAndRunnerCount,
            hue="type",palette= "plasma",
            linewidth=1,edgecolor="k"*len(df_WinnerAndRunnerCount))
plt.grid(True)
plt.legend(loc="center",prop={"size":15})
plt.title("Final Results by Country",color='r')
plt.show()


df_matches['Datetime'] = pd.to_datetime(df_matches['Datetime'])

df_matches['Datetime'] = df_matches['Datetime'].dt.date

#world_cup_matches[(df_matches.A == 1) & (df_matches.D == 6)]
df_matches_final = df_matches[(df_matches['Stage']=='Final')]

number_of_matches_home_wins = df_matches_final[(df_matches_final['Home Team Goals']> df_matches_final['Away Team Goals'])].shape[0]
number_of_matches_away_wins = df_matches_final[(df_matches_final['Home Team Goals']< df_matches_final['Away Team Goals'])].shape[0]
print(round(number_of_matches_home_wins/(number_of_matches_away_wins+number_of_matches_home_wins)*100,2),"% of home teams won the finals")

print("================================================")
print ("Overall Performance of Nations")
print("================================================")

df_WorldCups['Attendance'] = df_WorldCups['Attendance'].str.replace('\.', "").astype('int64') 
#Counting the countries who stood out victorious
winner = df_WorldCups['Winner'].value_counts() 
#Counting the countries who stood  at the second place in world cup
second_p = df_WorldCups['Runners-Up'].value_counts() 
#Counting the countries who stood  at the third place in world cup
third_p = df_WorldCups['Third'].value_counts() 
#Counting the countries who stood  at the fourth place in world cup
fourth_p = df_WorldCups['Fourth'].value_counts() 

#Concateneting the dataframes - Row-Wise for the winner, second place and third place
overall_result_df = pd.concat([winner,second_p,third_p,fourth_p], 
                               keys=['Champion','Second','Third','Fourth']).reset_index()

#Renaming the columns
overall_result_df.columns = ['Performance', 'Country','Count']
#Changing 'Germany FR" to "Germany"
overall_result_df['Country'] = overall_result_df['Country'].replace('Germany FR', 'Germany')
#tranforming the dataframe to plot - Pivoting Performance Variable, filling "NaNs" and sorting by the champion column.
overall_result_wide = overall_result_df.pivot_table(index='Country', 
                                                      columns='Performance', 
                                                      values='Count').fillna(0)

print (overall_result_wide.head(10))

overall_result_wide[['Champion','Second','Third','Fourth']].plot(kind='barh',layout=(1,4),subplots=True, sort_columns=True, legend=False,
                          figsize=(15,9), fontsize=10, sharex=True, sharey=True, title='Best countries - All World Cups')

plt.style.use('seaborn')
plt.show()

print("================================================")
print ("Team with maximum worldcup matches")
print("================================================")

print (df_WorldCups[df_WorldCups['Country'] == df_WorldCups['Winner']])

plt.figure(figsize=(13,7))
ax = plt.scatter("Year","GoalsScored",data= df_WorldCups,c=df_WorldCups["GoalsScored"],cmap="inferno",s=900,alpha=.7,linewidth=2,edgecolor="k")
plt.xticks(df_WorldCups["Year"].unique())
plt.yticks(np.arange(50,210,20))
plt.xlabel('Year',color='r')
plt.ylabel('Goals Scored',color='r')
plt.title('Goals scored Vs Year',color='b')
plt.ioff()

#Number of matches per each world cup.
df_WorldCups.plot(kind="line",x="Year",y="MatchesPlayed",color="blue",linewidth=1.5,grid=True,label="Matches Played",figsize=(10,10))
plt.xlabel("WC Years")
plt.ylabel("Numbers")
plt.title("Number of Matches per World Cup")
plt.legend()
plt.show()
#difference in the goals scored in home and away which results in the differnce and can analyse the skill of the team
df_matches['diff'] = df_matches['Home Team Goals']- df_matches['Away Team Goals']
print(df_matches.columns)
world_cup_matches_goal_difference = df_matches[['MatchID','Year','diff']]
world_cup_matches_goal_difference = world_cup_matches_goal_difference.dropna().drop_duplicates()
world_cup_matches_goal_difference = world_cup_matches_goal_difference.drop('MatchID',axis=1)
world_cup_matches_goal_difference['Year'] = world_cup_matches_goal_difference['Year'].astype(int)
world_cup_matches_goal_difference.boxplot(by='Year',figsize=(20,10))
plt.xticks(rotation=90)
plt.show()



plt.figure(figsize=(12,7))
sns.barplot(df_WorldCups["Year"],df_WorldCups["MatchesPlayed"],linewidth=1,
            edgecolor="k"*len(df_WorldCups),color="b",label="Total number of matches played")
sns.barplot(df_WorldCups["Year"],df_WorldCups["QualifiedTeams"],linewidth=1,
            edgecolor="k"*len(df_WorldCups),color="y",label="Total number of teams qualified teams")
plt.legend(loc="best",prop={"size":13})
plt.title("Qualified teams for each year",color='b')
plt.grid(True)
plt.ylabel("total number of matches and number of teams qualified for every year ")
plt.show()


#replace name in team name column German DR and Germany FR by Germany
#replace name of Soviet Union by Russia
def replace_name(df):
    if(df['Home Team Name'] in ['German DR', 'Germany FR']):
        df['Home Team Name'] = 'Germany'
    elif(df['Home Team Name'] == 'Soviet Union'):
        df['Home Team Name'] = 'Russia'
    
    if(df['Away Team Name'] in ['German DR', 'Germany FR']):
        df['Away Team Name'] = 'Germany'
    elif(df['Away Team Name'] == 'Soviet Union'):
        df['Away Team Name'] = 'Russia'
    return df
    
df_matches = df_matches.apply(replace_name, axis='columns')
print (df_matches)

#create a new dictionary of soccer team
team_name = {}
index = 0
for idx, row in df_matches.iterrows():
    name = row['Home Team Name']
    if(name not in team_name.keys()):
        team_name[name] = index
        index += 1
    name = row['Away Team Name']
    if(name not in team_name.keys()):
        team_name[name] = index
        index += 1
print("================================================")
print ("Dictionary of soccer team")
print("================================================")        
print (team_name)


#drop unecessary columns
dropped_matches = df_matches.drop(['Datetime', 'Stadium', 'Referee', 'Assistant 1', 'Assistant 2', 'RoundID','Win conditions',
             'Home Team Initials', 'Away Team Initials', 'Half-time Home Goals', 'Half-time Away Goals',
             'Attendance', 'City', 'MatchID', 'Stage'], 1)
#Make a series counting the number of time each team became World champion
championships = df_WorldCups['Winner'].map(lambda p: 'Germany' if p=='Germany FR' else p).value_counts()     

#append the value to the columns of 'Home Team Championships' and 'Away Team Championships' with Number of times being the champion of World Cup
dropped_matches['Home Team Championship'] = 0
dropped_matches['Away Team Championship'] = 0

def champion_count(df):
  if(championships.get(df['Home Team Name']) != None):
    df['Home Team Championship'] = championships.get(df['Home Team Name'])
  if(championships.get(df['Away Team Name']) != None):
    df['Away Team Championship'] = championships.get(df['Away Team Name'])
  return df


dropped_matches = dropped_matches.apply(champion_count, axis='columns')

#find who won: Home win: 1, Away win: 2, Draw: 0
dropped_matches['Winner'] = '-'

def find_winner(df):
    if(int(df['Home Team Goals']) == int(df['Away Team Goals'])):
        df['Winner'] = 0
    elif(int(df['Home Team Goals']) > int(df['Away Team Goals'])):
        df['Winner'] = 1
    else:
        df['Winner'] = 2
    return df

dropped_matches = dropped_matches.apply(find_winner, axis='columns')

#replace team name by id in team_name dictionary

def replace_team_name_by_id(df):
    df['Home Team Name'] = team_name[df['Home Team Name']]
    df['Away Team Name'] = team_name[df['Away Team Name']]
    return df

teamid_matches = dropped_matches.apply(replace_team_name_by_id, axis='columns')
#drop unecessary columns
teamid_matches = teamid_matches.drop(['Year', 'Home Team Goals', 'Away Team Goals'], 1)


   


