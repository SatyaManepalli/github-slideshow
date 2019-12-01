# -*- coding: utf-8 -*-
"""
Created on Sun May  5 07:47:51 2019

@author: Satya Manepalli
"""

import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt


import warnings
warnings.filterwarnings("ignore")

#ImportingData 
PlayerData = pd.read_csv(r"C:\DataScience\In Class\fifa-18-demo-player-dataset\CompleteDataset.csv")
#CompletePlayerData
print (PlayerData)
#OutOfAll The Player Data in CSV file Acquiring only The columns that we require 
PlayerData = PlayerData[['Name', 'Age', 'Nationality', 'Overall', 'Wage', 'Potential', 'Club', 'Value', 'Preferred Positions']]
print (PlayerData.head(5))
#Creating a new parameter for Growth = Potential - Overall to asses the growth of the skill of the player
PlayerData['Growth'] = PlayerData['Potential'] - PlayerData['Overall']
print (PlayerData)

#finding the mean values of growth, overall and potential of the players


#Plotting the age boxplot and distribution for players
#Age Distribution of Players
fig, axes = plt.subplots(2)
sns.boxplot(x="Age", data=PlayerData, ax=axes[0])
sns.distplot(PlayerData["Age"], bins=len(PlayerData["Age"].value_counts().sort_index().index), ax=axes[1])
axes[1].set_xlim(min(PlayerData["Age"])-1, max(PlayerData["Age"]))
axes[0].set_xticks(range(min(PlayerData["Age"]), max(PlayerData["Age"])+1))
axes[1].set_xticks(range(min(PlayerData["Age"]), max(PlayerData["Age"])+1))
fig.tight_layout()
plt.show()

# Overall ratings
fig, axe = plt.subplots()
ax = sns.distplot(PlayerData["Overall"], bins=len(PlayerData["Overall"].value_counts().index))
ax.set_xticks(range(0, 100, 5))
ax.set_xlim(0,100)
ax.set_xlabel("Overall Rating")
fig.tight_layout()

#we are interested in seeing which type of offensive players tends to get paid the most: the striker, the right-winger, or the left-winger.
#Multivariate scatter plots

footballers = PlayerData.copy()
footballers['Unit'] = PlayerData['Value'].str[-1]
footballers['Value (M)'] = np.where(footballers['Unit'] == '0', 0, 
                                    footballers['Value'].str[1:-1].replace(r'[a-zA-Z]',''))
footballers['Value (M)'] = footballers['Value (M)'].astype(float)
footballers['Value (M)'] = np.where(footballers['Unit'] == 'M', 
                                    footballers['Value (M)'], 
                                    footballers['Value (M)']/1000)
footballers = footballers.assign(Value=footballers['Value (M)'],
                                 Position=footballers['Preferred Positions'].str.split().str[0])

sns.lmplot(x='Value', y='Overall', hue='Position', 
           data=footballers.loc[footballers['Position'].isin(['ST', 'RW', 'LW'])], 
           fit_reg=False)

#do Strikers score higher on "Aggression" than Goalkeepers do?
PlayerData['AgeRange'] = pd.cut(PlayerData.Age, bins = [0,23,33,45],labels = ['Young','Mature','Old'])
plt.figure(figsize=(16,8))
plt.title("Percentages of Young, Mature, and Old Players", fontsize = 20, fontweight = 'bold')
labels = 'Mature','Young','Old'
plt.rcParams['font.size'] = 20.0
plt.pie(PlayerData.AgeRange.value_counts(), labels = labels, autopct='%1.1f%%', startangle=0)
plt.axis('equal')
plt.show()

top20_nation = PlayerData.groupby('Nationality').size().reset_index(name='Count').sort_values('Count',ascending = False)[:20]
print(top20_nation)

plt.figure(figsize=(16,20))

countries = list(top20_nation.loc[::-1,'Nationality'])
pos = np.arange(len(countries))
count = list(top20_nation.loc[::-1,'Count'])

plt.barh(pos, count, align='center', alpha=.8)
plt.yticks(pos, countries, fontsize=25)
plt.xlabel('Count', fontsize=25)
plt.title('Number players by Countries', fontsize=30, fontweight='bold')
 
plt.show()

def get_top20_players(country):
    top20players = PlayerData[PlayerData.Nationality == country].sort_values('Value',ascending = False)[:20]
    return top20players

top10_nation_list = top20_nation.Nationality[:10].tolist()

frames = []
for i in range(len(top10_nation_list)):
    temp_df = get_top20_players(top10_nation_list[i])
    frames.append(temp_df)
top_players_in_top10 = pd.concat(frames)
top_players_in_top10

fifa_growth = PlayerData.groupby(['Age'])['Growth'].mean()
fifa_overall = PlayerData.groupby(['Age'])['Overall'].mean()
fifa_potential = PlayerData.groupby(['Age'])['Potential'].mean()

summary = pd.concat([fifa_growth, fifa_overall, fifa_potential], axis=1)

axis = summary.plot()
axis.set_ylabel('Rating Points')
axis.set_title('Average Growth Potential by Age')

#Let's find clubs with most players rated over 85
'''cutoff = 85
players = PlayerData[PlayerData['Overall']>cutoff]
grouped_players = PlayerData[PlayerData['Overall']>cutoff].groupby('Club')
number_of_players = grouped_players.count()['Name'].sort_values(ascending = False)

ax = sns.countplot(x = 'Club', data = players, order = number_of_players.index)

ax.set_xticklabels(labels = number_of_players.index, rotation='vertical')
ax.set_ylabel('Number of players (Over 90)')
ax.set_xlabel('Club')
ax.set_title('Top players (Overall > %.i)' %cutoff)'''


def extract_value_from(value):
    out = value.replace('€', '')
    if 'M' in out:
        out = float(out.replace('M', ''))*1000000
    elif 'K' in value:
        out = float(out.replace('K', ''))*1000
    return float(out)

PlayerData['Value'] = PlayerData['Value'].apply(lambda x: extract_value_from(x))
PlayerData['Wage'] = PlayerData['Wage'].apply(lambda x: extract_value_from(x))

fifa_wage = PlayerData.groupby(['Overall'])['Wage'].mean()
fifa_value = PlayerData.groupby(['Overall'])['Value'].mean()
fifa_wage = fifa_wage.apply(lambda x: x/1000)
fifa_value = fifa_value.apply(lambda x: x/1000000)
PlayerData["Wage(by Potential)"] = PlayerData["Wage"]
PlayerData["Value(by Potential)"] = PlayerData["Value"]
fifa_wage_p = PlayerData.groupby(['Potential'])['Wage(by Potential)'].mean()
fifa_value_p = PlayerData.groupby(['Potential'])['Value(by Potential)'].mean()
fifa_wage_p = fifa_wage_p.apply(lambda x: x/1000)
fifa_value_p = fifa_value_p.apply(lambda x: x/1000000)
summary = pd.concat([fifa_wage, fifa_value, fifa_wage_p, fifa_value_p], axis=1)

axis = summary.plot()
axis.set_ylabel('Wage / Value')
axis.set_title('Average Wage / Value by Rating')

fifa_wage_a = PlayerData.groupby(['Age'])['Wage'].mean()
fifa_value_a = PlayerData.groupby(['Age'])['Value'].mean()
fifa_wage_a = fifa_wage_a.apply(lambda x: x/1000)
fifa_value_a = fifa_value_a.apply(lambda x: x/1000000)
summary = pd.concat([fifa_wage_a, fifa_value_a], axis=1)

axis = summary.plot()
axis.set_ylabel('Wage / Value')
axis.set_title('Average Age')


'''plt.figure(figsize=(16,16))
sns.set_style("whitegrid")
plt.title('Relationship between Value, Overall and Age', fontsize=30, fontweight='bold', y=1.05,)
plt.xlabel('Age', fontsize=25)
plt.ylabel('Overall', fontsize=25)

plt.figure(figsize=(16,8))
sns.set_style("whitegrid")
plt.title('Grouping players by Preffered Position', fontsize=20, fontweight='bold', y=1.05,)
plt.xlabel('Number of players', fontsize=15)
plt.ylabel('Players Age', fontsize=15)
sns.countplot(x="Position", data=PlayerData, palette="hls");
plt.show()'''

