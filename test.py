import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data organized into a dictionary format
data = {
    "1992": {
        "proportional_votes": {'BUSH, GEORGE H.W.': 202.01426170551423, 'CLINTON, BILL': 230.4224465409085, 'PEROT, ROSS': 101.27103312436545},
        "winner_take_all": {'BUSH, GEORGE H.W.': 168.0, 'CLINTON, BILL': 370.0, 'PEROT, ROSS': 0},
        "popular_vote_percentage": {'BUSH, GEORGE H.W.': 201.1274128492431, 'CLINTON, BILL': 231.2186030792799, 'PEROT, ROSS': 101.43863205066015},
    },
    "1996": {
        "proportional_votes": {'DOLE, ROBERT': 219.95170532593082, 'CLINTON, BILL': 263.30765057511974, 'PEROT, ROSS': 42.046327210454955},
        "winner_take_all": {'DOLE, ROBERT': 159.0, 'CLINTON, BILL': 379.0, 'PEROT, ROSS': 0},
        "popular_vote_percentage": {'DOLE, ROBERT': 218.78642115498133, 'CLINTON, BILL': 264.57380720440824, 'PEROT, ROSS': 42.094016610758615},
    },
    "2000": {
        "proportional_votes": {'BUSH, GEORGE W.': 258.89318577379476, 'GORE, AL': 257.73629073034635, 'NADER, RALPH': 13.097658504769171},
        "winner_take_all": {'BUSH, GEORGE W.': 271.0, 'GORE, AL': 267.0, 'NADER, RALPH': 0},
        "popular_vote_percentage": {'BUSH, GEORGE W.': 257.07354157739786, 'GORE, AL': 259.8242895698355, 'NADER, RALPH': 12.952288265821815},
    },
    "2004": {
        "proportional_votes": {'BUSH, GEORGE W.': 274.42779825637024, 'KERRY, JOHN': 257.70434704624444},
        "winner_take_all": {'BUSH, GEORGE W.': 286.0, 'KERRY, JOHN': 252.0},
        "popular_vote_percentage": {'BUSH, GEORGE W.': 272.75330890330935, 'KERRY, JOHN': 259.56068050980207},
    },
    "2008": {
        "proportional_votes": {'MCCAIN, JOHN': 246.57023154216995, 'OBAMA, BARACK H.': 283.1661460551467},
        "winner_take_all": {'MCCAIN, JOHN': 174.0, 'OBAMA, BARACK H.': 364.0},
        "popular_vote_percentage": {'MCCAIN, JOHN': 245.41439338420224, 'OBAMA, BARACK H.': 284.5106031914517},
    },
    "2012": {
        "proportional_votes": {'ROMNEY, MITT': 256.0369283166712, 'OBAMA, BARACK H.': 272.0175691670548},
        "winner_take_all": {'ROMNEY, MITT': 206.0, 'OBAMA, BARACK H.': 332.0},
        "popular_vote_percentage": {'ROMNEY, MITT': 253.84465338031563, 'OBAMA, BARACK H.': 274.5393983554142},
    },
    "2016": {
        "proportional_votes": {'TRUMP, DONALD J.': 249.64389878344622, 'CLINTON, HILLARY': 255.84377512972898, 'JOHNSON, GARY': 17.189180134283745, 'STEIN, JILL': 5.5041905030778775},
        "winner_take_all": {'TRUMP, DONALD J.': 305.0, 'CLINTON, HILLARY': 233.0, 'JOHNSON, GARY': 0, 'STEIN, JILL': 0},
        "popular_vote_percentage": {'TRUMP, DONALD J.': 247.72761323032398, 'CLINTON, HILLARY': 259.0098338523476, 'JOHNSON, GARY': 16.693430416110537, 'STEIN, JILL': 5.479441506462151},
    },
}

# Convert data to DataFrames
years = list(data.keys())
candidates = set([candidate for year_data in data.values() for vote_type in year_data.values() for candidate in vote_type])

def get_votes_by_type(vote_type):
    return pd.DataFrame({year: {candidate: data[year][vote_type].get(candidate, 0) for candidate in candidates} for year in years})

proportional_df = get_votes_by_type("proportional_votes")
winner_take_all_df = get_votes_by_type("winner_take_all")
popular_vote_df = get_votes_by_type("popular_vote_percentage")

# Set up the figure
fig, ax = plt.subplots(figsize=(14, 8))

# Define bar width and positions
bar_width = 0.25
indices = np.arange(len(years))

# Plot each type of vote with an offset
for i, (df, label) in enumerate(zip([proportional_df, winner_take_all_df, popular_vote_df],
                                    ["Proportional Votes", "Winner-Take-All Votes", "Popular Vote Percentage"])):
    bottom = np.zeros(len(years))
    for candidate in candidates:
        ax.bar(indices + i * bar_width, df.loc[candidate], bar_width, label=f"{label} - {candidate}" if i == 0 else "", bottom=bottom)
        bottom += df.loc[candidate].values

# Set labels and title
ax.set_xticks(indices + bar_width)
ax.set_xticklabels(years)
ax.set_xlabel("Year")
ax.set_ylabel("Votes")
ax.set_ylim(100, 400)
ax.set_title("Vote Distribution by Year (Proportional, Winner-Take-All, Popular Vote Percentage)")
ax.legend(loc="upper left", bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()
