This directory will contain any jupyter notebook/python files used to analyze the data.
### Descriptions of Files
## initial_clean.py
- Imports the Dataset from a local csv file
- Removes any unnecesary information, like columns and results from Independent and Green party candidates
## determine_winner_by_county.py
This was part of the EDA, and consists of code that returns a dataframe with information on whether the Democratic candidate won each county. It was easier to use this one dimensional metric for a county's vote, since it's easy to invert a boolean for any other use. This step showed me that my research question is valid and achievable
## visualizations.py
This is fairly straightforward, this script created the visualizations in the images folder
## final.py
This script pulled in the data about whether each county voted for the Democratic candidate in each election and combined it with a dataFrame of my creation that represents whether the Democrat won the entire Presidential data. With the two DataFrames mergeed, it was possible to determine how many times each county voted for the winner of the election. I then sorted the counties by amount of correct predictions, and then cut off all the counties that got less than 5 (out of the past 5) elections correct. This final list is seen in data/processed
### EDA
## First Step
I shaved down the dataset and after a lot of wrangling, created a DataFrame that contains every county, and records whether it voted for the Democratic candidate in every election from 2000-2016. This isn't quite the final result, but it brings the final analysis within reach, I'll only need to create a frame that defines whether the Democrat won in each year
## Visualizations
My project doesn't benefit from visualizations that can be realistically created by someone with limited knowledge of how to create them. I'd need a national map of the US, with every county as a point on that map to make something useful. I've included a couple visualizations in visualizations.py, and while they definitely are interesting and pertain to my topic, they're not directly applicable to my research question.
