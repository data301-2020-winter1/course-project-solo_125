[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=313856&assignment_repo_type=GroupAssignmentRepo)
# Group 125 - Which counties determine the Presidency?

## Final Results in data/processed

## Milestones

Details for Milestone are available on Canvas (left sidebar, Course Project) or [here](https://firas.moosvi.com/courses/data301/project/milestone01.html).

## Describe your topic/interest in about 150-200 words

My topic focuses on the bellwether status of various US counties. Counties don't elect the president directly, but voters in a county representative of the US can serve as an early indication of where the presidential race is headed. I was interested in finding out which counties have picked the President in the past 5 elections (excluding 2020). I picked this topic before the 2020 election, so I was curious which counties to watch on election night.

## Describe your dataset in about 150-200 words

This dataset comes from the Harvard Dataverse, and was originally compiled by the MIT Election Data and Science Lab. It contains roughly 50,000 lines with every county in the US, and how many votes were cast in each for the Democratic, Republican, and Green parties, as well as a line for Independents. It also has a column with the total amount of votes cast, allowing for the calculation of the winner in each county.

### EDA
## First Step
I shaved down the dataset and after a lot of wrangling, created a DataFrame that contains every county, and records whether it voted for the Democratic candidate in every election from 2000-2016. This isn't quite the final result, but it brings the final analysis within reach, I'll only need to create a frame that defines whether the Democrat won in each year
## Visualizations
My project doesn't benefit from visualizations that can be realistically created by someone with limited knowledge of how to create them. I'd need a national map of the US, with every county as a point on that map to make something useful. I've included a couple visualizations in visualizations.py, and while they definitely are interesting and pertain to my topic, they're not directly applicable to my research question.


## Team Members

- Hi! My name is Ilya Yereferenko and I'm the only person in this group!
## References

https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/VOQCHQ
