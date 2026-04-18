# import pyreadr

# abbeviations_to_states = {
#     "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA": "California", "CO": "Colorado",
#     "CT": "Connecticut", "DE": "Delaware", "FL": "Florida", "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho",
#     "IL": "Illinois", "IN": "Indiana", "IA": "Iowa", "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana",
#     "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi",
#     "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada", "NH": "New Hampshire", "NJ": "New Jersey",
#     "NM": "New Mexico", "NY": "New York", "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma",
#     "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina", "SD": "South Dakota",
#     "TN": "Tennessee", "TX": "Texas", "UT": "Utah", "VT": "Vermont", "VA": "Virginia", "WA": "Washington",
#     "WV": "West Virginia", "WI": "Wisconsin", "WY": "Wyoming", "DC": "D.C."
# }
# years_to_show = [2020]

# result = pyreadr.read_r('./dataverse_shareable_presidential_county_returns_1868_2020.Rdata')
# result = result['pres_elections_release']
# print(result.columns)
# print(result)
# for year in years_to_show:
#     # print(result["state"].unique())
#     # print(result["state"].tolist())
#     for abbr, state in abbeviations_to_states.items():
#         per_state = result[(result["state"] == abbr) & (result["election_year"] == year)]
#         # print(per_state[["democratic_raw_votes", "republican_raw_votes", "raw_county_vote_totals"]])
#         print(abbr, per_state["democratic_raw_votes"].sum() / per_state["raw_county_vote_totals"].sum(), per_state["republican_raw_votes"].sum() / per_state["raw_county_vote_totals"].sum())
# # print(result["dem_nominee"].unique())
# print(result.iloc[0])
# # print(result[["pres_raw_county_vote_totals_two_party", "raw_county_vote_totals"]])

# https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/42MVDX
import pandas as pd
import math
import altair as alt

years_to_show = [1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]
# years_to_show = [2020]
parties = ['REPUBLICAN', 'DEMOCRAT', 'GREEN', 'LIBERTARIAN', 'INDEPENDENT']


def candidate_to_popular_vote(per_year, candidate):
    return per_year[per_year["candidate"] == candidate]["candidatevotes"].sum()

def is_valid_candidate(candidate):
    return isinstance(candidate, str) and candidate != "OTHER"

state_to_votes = pd.read_csv("./Electoral_College.csv")
df = pd.read_csv("./1976-2020-president.csv")
states = df["state"].unique()
candidate_to_party = {}
output_dfs = []
for year in years_to_show:
    # per_year = df[(df["year"] == year) & (df["party_simplified"] != "OTHER")]
    per_year = df[df["year"] == year]
    all_candidates = list(filter(is_valid_candidate, per_year["candidate"].unique()))
    total_votes = per_year["candidatevotes"].sum()

    popular_vote_unfilt = {candidate: candidate_to_popular_vote(per_year, candidate) for candidate in all_candidates}
    popular_vote = {candidate: popular_vote_unfilt[candidate] for candidate in all_candidates if candidate_to_popular_vote(per_year, candidate) > .01 * total_votes}
    candidates_filt = list(popular_vote.keys())
    winner_take_all = {candidate: 0 for candidate in candidates_filt}
    proportional_votes = {candidate: 0 for candidate in candidates_filt}
    popular_vote_percentage = {candidate: 538 * popular_vote[candidate] / total_votes for candidate in candidates_filt}

    for state in states:
        converted_state_name = state.title() if state != "DISTRICT OF COLUMBIA" else "D.C."
        votes = state_to_votes[(state_to_votes["State"] == converted_state_name) & (state_to_votes["Year"] == year)]
        if len(votes) != 1:
            raise ValueError(f"Invalid number of votes for {converted_state_name}")
        nvotes = votes["Votes"].iloc[0]
        per_state = per_year[per_year["state"] == state]
        for _, row in per_state.iterrows():
            if row["candidate"] not in proportional_votes:
                continue
            # raise ValueError(row)
            candidate_to_party[row["candidate"]] = row["party_detailed"]
            proportional_votes[row["candidate"]] += nvotes * row["candidatevotes"] / row["totalvotes"]
            if row["candidatevotes"] == per_state["candidatevotes"].max():
                winner_take_all[row["candidate"]] += nvotes
    def fmt(d):
        return {k: round(float(v), 1) for k, v in d.items()}
    print(year)
    print(f"proportional_votes={fmt(proportional_votes)}")
    print(f"winner_take_all={fmt(winner_take_all)}")
    print(f"popular_vote_percentage={fmt(popular_vote_percentage)}")
    print()
    output_dfs.append(pd.DataFrame({
        "proportional_votes": [proportional_votes[candidate] for candidate in candidates_filt],
        "winner_take_all": [winner_take_all[candidate] for candidate in candidates_filt],
        "popular_vote_percentage": [popular_vote_percentage[candidate] for candidate in candidates_filt],
    }))
