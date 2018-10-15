
## US Flight Data Analysis for 2008

Initial Version: https://public.tableau.com/profile/doibajit.medhi#!/vizhome/Flight-Data-2008/Story1?publish=yes

Final Version: https://public.tableau.com/profile/doibajit.medhi#!/vizhome/Flight-Data-2008-Final/Story1?publish=yes


### Summary

Data Source : http://stat-computing.org/dataexpo/2009/the-data.html

Supplemental data : http://stat-computing.org/dataexpo/2009/supplemental-data.html
                    (Airports.csv and carriers.csv)

The data comes originally from RITA where it is described in detail. You can download the data there, or from the bzipped csv files listed below. These files have derivable variables removed, are packaged in yearly chunks and have been more heavily compressed than the originals.

For my project, I have selected the 2008 year as the dataset. 


### Design

I have joined two more datasets to collect information regarding the Airline names and Airport location.

My Tableau story is an attempt in understanding the relationship between number of flights, average delay, type of delays, and other airline and airport information in the dataset. This data is limited by the 2008 year. (Adding additional year data is too large for the Tableau public to upload)

Few of my Conclusions from this analysis:

Atlanta,Chicago and Dallas Fort Worth are the top 3 most popular airports among the origin or destination airports.

Southwest topped the 2008 year with maximum flights and also the total delay in minutes.

Cancelled/Diverted Flights increase at the start of the year around February. The graph shows a decline until June which  is Summer time travel. The numbers fall during the later month peaking again during the holiday season around christmas.From a flying customer perspective, flying with Aloha Airlines is the best choice. Aloha had the lowest number of cancelled flights. The major airlines like American,American Eagle,Southwest, Skywest and United were in the top 5 for cancellation/delayed flights.

The top 3 delays over the course of the year are Average carrier delay, Average Late Aircraft delay and Average NAS delay. The graph show increase in the month of February, June, July and December. This is similar to the pattern with the cancelled/diverted flights we saw earlier.It appears Southwest, American and American Eagle have consistent total delay over the course of the year except during the fall months of September and October. The numbers increase again during the winter holiday season.

The average arrival and departure delays are generally higher during the summer travel time(June-July) and the winter holiday season (December)

The average arrival and departure delay shows the increase during February,June,July and December months. This is a similar pattern we saw across earlier. Overall, Nantucket Memorial, Chicago Midway, Pierre Regional, Pueblo Memorial and Klamath Falls International Airports have higher average arrival/departure delays over the entire year.

Design Choices:

In the first slide, Distribution of Flights for year 2008 by US Airports I used the 'packed bubble' option along with size scheme estimator to show which origin/destination had the most number of flights. Although, color scheme is not adding any information, I am still using it as I believe this makes the plot visually better than just using one color. I think the color
makes the plot more interactive. 

The second slide is about Flights flown by US airlines for the year 2008 and delays associated with each airline. This is a simple bar chart with the Airline name shown horizontally. I did not use color scheme as only one variable is being shown for each graph.

The third slide is about the Cancelled and Delayed Flights data over time and also by individual airline. A line chart was used for the time graph as that is the simplest elegant way to show changes.I also used a dual-axis to overlap both lines(with different color) to show changes over time. Additionally, to filter the same line graph by airline, I plotted using the horizontal bars with different colors scheme for the two variables.

The next slide is about representation of various delays shown using a bar chart with color scheme. The upper chart is the various delays over the months of the year. The lower chart is the various delays by airline over the course of the year.

The last one is about Geographical representation of Airports and their average arrival and departure delay using the maps display. There is a month filter for analysing changes over the course of the year. 


### Feedback

Here is a slide by slide critique:

1) Add what questions you are trying to answer

2) Captions just stating what to do or what you have done are not enough. What is the main conclusion a reader should take from   your slide? Why are they looking at it? Add that to all of your captions.

3) These should be horizontal bar charts so people can read the airlines. What are the units for the delay graph? Change the top   y-axis label to 'Number of flights'. Never use a label that says 'Count of ...'. Make sure to change it to something as easily   understood as possible.

4) Put the month names on the x-axis. Also, you do not need a month filter if the x-axis is in months.

5) What are the units for either graph? You need to add them. Also, change the top y axis label to something else. 'Value' is     not helpful'

6) Get rid of the total delay filter.


I have taken the above feedback and incorporated in my final version. I have also formatted my tableau story with a color scheme. The text,captions have also been formatted for each slides.


### Resources

Google

Slack

StackOverflow

Udacity Course Videos and Quizzes

Tableau Public Documentation

Udacity Reviewer Feedback.

