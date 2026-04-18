# US Electoral College Reform Analysis

This project simulates US presidential elections (1992–2020) under three different voting systems to explore how electoral outcomes would change under alternative rules.

## Motivation

The current winner-take-all Electoral College has a well-known flaw: candidates only campaign in swing states. Californians and New Yorkers are just as politically irrelevant as voters in Wyoming or North Dakota. The common criticism of a national popular vote is that candidates would ignore rural areas and focus entirely on big cities. But that's essentially what happens now, just with swing-state cities instead.

A **proportional Electoral College** offers a middle ground: each state still has its weighted electoral votes (preserving some rural representation), but those votes are split proportionally based on the actual votes cast in that state. Candidates would have reason to campaign everywhere, not just in Pennsylvania and Arizona.

## The Three Systems

| System | Description |
|---|---|
| **Winner-take-all** | Current system. All of a state's electoral votes go to the plurality winner. |
| **Proportional** | Electoral votes are split proportionally by vote share within each state. |
| **Popular vote %** | Each candidate receives electoral votes proportional to their share of the total national popular vote (538 × vote share). |

## Results

### 1992
| Candidate | Proportional | Winner-take-all | Popular Vote % |
|---|---|---|---|
| Clinton, Bill | 230.4 | 370.0 | 231.2 |
| Bush, George H.W. | 202.0 | 168.0 | 201.1 |
| Perot, Ross | 101.3 | 0.0 | 101.4 |

### 1996
| Candidate | Proportional | Winner-take-all | Popular Vote % |
|---|---|---|---|
| Clinton, Bill | 263.3 | 379.0 | 264.6 |
| Dole, Robert | 220.0 | 159.0 | 218.8 |
| Perot, Ross | 42.0 | 0.0 | 42.1 |

### 2000
| Candidate | Proportional | Winner-take-all | Popular Vote % |
|---|---|---|---|
| Bush, George W. | 258.9 | 271.0 | 257.1 |
| Gore, Al | 257.7 | 267.0 | 259.8 |
| Nader, Ralph | 13.1 | 0.0 | 13.0 |

Under winner-take-all, Bush won by a single state (Florida, decided by 537 votes). Under both proportional and popular vote systems, Bush still leads — but only narrowly, and the hanging chad controversy would not have been capable of flipping the entire election.

### 2004
| Candidate | Proportional | Winner-take-all | Popular Vote % |
|---|---|---|---|
| Bush, George W. | 274.4 | 286.0 | 272.8 |
| Kerry, John | 257.7 | 252.0 | 259.6 |

### 2008
| Candidate | Proportional | Winner-take-all | Popular Vote % |
|---|---|---|---|
| Obama, Barack H. | 283.2 | 364.0 | 284.5 |
| McCain, John | 246.6 | 174.0 | 245.4 |

### 2012
| Candidate | Proportional | Winner-take-all | Popular Vote % |
|---|---|---|---|
| Obama, Barack H. | 272.0 | 332.0 | 274.5 |
| Romney, Mitt | 256.0 | 206.0 | 253.8 |

### 2016
| Candidate | Proportional | Winner-take-all | Popular Vote % |
|---|---|---|---|
| Clinton, Hillary | **255.8** | 233.0 | **259.0** |
| Trump, Donald J. | 249.6 | **305.0** | 247.7 |
| Johnson, Gary | 17.2 | 0.0 | 16.7 |
| Stein, Jill | 5.5 | 0.0 | 5.5 |

The starkest example of electoral distortion: Clinton won the popular vote by nearly 3 million votes, and would have won under both alternative systems, yet lost the Electoral College 305–233.

### 2020
| Candidate | Proportional | Winner-take-all | Popular Vote % |
|---|---|---|---|
| Biden, Joseph R. Jr | 273.0 | 306.0 | 275.8 |
| Trump, Donald J. | 254.3 | 232.0 | 251.9 |
| Jorgensen, Jo | 6.5 | 0.0 | 6.3 |

## Data Sources

- [MIT Election Data and Science Lab — 1976–2020 U.S. President](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/42MVDX)
- Electoral College vote counts by state and year: `Electoral_College.csv`

## Running

```bash
pip install pandas altair
python main.py
```
