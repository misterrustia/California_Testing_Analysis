# California_Testing_Analysis
California Smart Balance Test scores regression analysis
California Testing Analysis documentation

## Problem statement

With the pandemic closing school sites and no standardized testing occurring for the 2020 school year the 2021 CAASPP California Assessment of Student Performance and Progress 
Are the first state reported scores since 2019. Education is a complex and intricate part of our society. The best way to assess performance of students throughout their educational journey will always be up for debate, but since the adoption of the Smarter Balanced Summative Assessments in California there has been consistent data that can be used to gain insight into the state of student performance. I built a model to predict the Mean Scale Score per demographic at each school site using multiple data sources. My goal was to better understand what quantifiable factors have an influence in student CAASPP scores and predict how the change in key features would affect test scores. 

## Data wrangling

With the goal of predicting student test scores a wider view of the community, school and district was required to create a data set with descriptive features that could allow for quality predictions. Multiple sources are used to generate the final data set. Cleaning and joining of sources was broken down into multiple notebooks to isolate each source's cleaning and joining with other data sets. English Language Arts/Literacy and Mathematics student test scores from the 2021 CAASPP contain the target Mean Test Score feature that the final model predicts. The Target feature ‘Mean Scale Score’ is for a specific student group at the school site(ex: ‘Filipino’ )

Other data sources included 
Census population and poverty data by zip code.
Yelp api data on the nearest grocery store and amount of grocery stores in 3 miles.
District level salary data
Average housing price data by zip code
School site student demographic and student teacher ratio data. 
After cleaning and joining all of these diverse data sets together there were just over 300,000 student group Mean Scale Score data points to observe in the exploratory Data Analysis. 



## Exploratory Data Analysis
Once all of the data sources were combined exploration of the feature distributions were taken. To get some perspective on the scores across the state, county averages were created using pandas groupby. Scatter plots of average housing price 2021 by  Mean Scale score, colored by quartile start to build a picture of the distribution of districts in the state. 
