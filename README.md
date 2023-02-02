# California Testing Analysis documentation

## Introduction

With the pandemic closing school sites and no standardized testing occurring for the 2020 school year, the 2021 CAASPP California Assessment of Student Performance and Progress, 
are the first state-reported test scores since 2019. Education is a complex and intricate part of our society, and the best way to assess student's performance throughout their educational journey will always be up for debate. Since the adoption of the Smarter Balanced Summative Assessments in California, there has been consistent data that could be used to gain insight into the state of student performance. Using multiple data sources, I built a model to predict the Mean Scale Score per student demographic at the school site level. My goal is to understand what quantifiable factors influence student 2021 CAASPP scores and predict how the change in the key features I uncover affects test scores. 

## Data Wrangling 

To predict student test scores, a more comprehensive view of the community, school, and district was required to create a data set with descriptive features that could allow for quality predictions. Multiple data sources were joined together to generate the final data set. The keep process of joining the data sources clear, cleaning, and joining the data was broken down into chronological notebooks to isolate each source's cleaning and joining with other data sets. 

### Data sources included 
- Census population and poverty data by zip code
- Yelp API data on the nearest grocery store and amount of grocery stores in 3 miles
- District-level salary data
- Average housing price data by zip code
- School site student demographic and student-teacher ratio data 

After cleaning and joining all of these diverse data sets together, there were just over 300,000 student group Mean Scale Score data points to observe in the exploratory Data Analysis. 
