
INST126 Project 4 COVID-19 Tracker

UPDATE 1 (11/25/2020):
Project Goal:
Project goal is to create a thorough and detailed analysis covid cases, peaks and troughs in various counties, deaths vs recoveries, etc.


This project will use python pandas data analysis visualization tool to present COVID-19 Data. In regards to the code, we first need to index the data values, 
clean the data set, drop all extraneous values, and then drop all null values in the dataset. Pandas has various functions such as the dropna() and set_clean()
function to help us with this. The dataset will be collected by the part of our team tasked with research.

we plan to seperate various graphs, which represent different data, into functions. The user will get to pick which function they would like to run
As of now, we have 3 functions planned: Function to create a graph showcasing cases in days and months, fucntion to create a graph showcasing number of recorded 
recoveries in days and months, and a function showcasing deaths due to COVID-19 in days and months.

Each function will sort data by day and month, choose an appropriate range, then display the information. There could be plans in the future to seperate the days and months
into seperate functions as well.
n easily use the program and inte
A strong focus here is to make the data easy and accessible, meaning anyone carpret the graphs.

UPDATE 2 (12/2/2020):

We plan to seperate various graphs, which represent different data, into functions. The user will get to pick which function they would like to run
As of now, we have 2 functions planned for covid data: The first covid_deaths() is data  showcasing cases by state and or county and covid_cases() shows cases by state or county. We have an additional 2 functions that will allow the user to decide how they will view their data. One function, set_range() will set the range for the matplot graph and the second function, displaf(df) will take values from set_range() function and present them in the visual form the user wants. 

Furthermore, there will be a variable 'selection' which will ask the user input with two choices; Covid deaths or Covid cases. This variable will be set to lowercase using the .lower() function. There will be if statements conditionals to be used. When the user picks the Covid deaths choice, the covid_deaths() function will be called. Likewise, when the user picks Covid cases, covid_cases() function will be called. Otherwise, when the user inputs anything other than the above choices, a message "Invalid Selection" will be shown.

Update 3 (12/9/20):

We have made a "COVID 19 Tracker" that tracks data specifically from the state of Maryland. We derived this data from a .csv file that has a record of every case in every county throughout the state. Not only this, it also contains each COVID death and the corresponding dates of positive tests. Using this data we were able to make user specified graphs depending on how the user wanted the data to be presented.

We decided to implement this data in the form of two graphs one being the number of cases per month and the other being deaths per month. Both graphs can be presented to the user as a line graph, a bar graph, or a scatter plot (this is only recommended to be used when examining just one month). 

In order to do this we had to create a county selector for the user using while loops to make sure the state selected was in fact Maryland. Next the user was required to input a county in Maryland that could be tracked. Next the user was prompted to select cases or deaths but is later given the option for both. The user must also select a date range in which they would like to see the visualization according to days and months. This was also done using while loops and conditionals. Lastly, the display function asks the user which type of graph they would like to display. 
The display function was created using the Matplotlib library which enabled us to use a wide range of graphs that were customizable to our specific needs. 
Our selection function is still in place, and we successfully made a user driven COVID tracker visualization.
