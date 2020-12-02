
INST126 Project 4 COVID-19 Tracker

UPDATE 1 (11/25/2020):
Project Goal:
Project goal is to create a thorough and detailed analysis covid cases, peaks and troughs in various counties, deaths vs recoveries, etc.


This project will use python pandas data analysis visualization tool to present COVID-19 Data. In regards to the code, we first need to index the data values, 
clean the data set, drop all extraneous values, and then drop all null values in the dataset. Pandas has various functions such as the dropna() and set_clean()
function to help us with this. The dataset will be collected by the part of our team tasked with research.

We plan to seperate various graphs, which represent different data, into functions. The user will get to pick which function they would like to run
As of now, we have 2 functions planned for covid data: The first covid_deaths() is data  showcasing cases by state and or county and covid_cases() shows cases by state or county. We have an additional 2 functions that will allow the user to decide how they will view their data. One function, set_range() will set the range for the matplot graph and the second function, displaf(df) will take values from set_range() function and present them in the visual form the user wants. 

Each function will sort data by day or month, choose an appropriate range, then display the information. There could be plans in the future to seperate the days and months
into seperate functions as well.

A strong focus here is to make the data easy and accessible, meaning anyone can easily use the program and interpret the graphs.

UPDATE 2 (12/2/2020):

We plan to seperate various graphs, which represent different data, into functions. The user will get to pick which function they would like to run
As of now, we have 2 functions planned for covid data: The first covid_deaths() is data  showcasing cases by state and or county and covid_cases() shows cases by state or county. We have an additional 2 functions that will allow the user to decide how they will view their data. One function, set_range() will set the range for the matplot graph and the second function, displaf(df) will take values from set_range() function and present them in the visual form the user wants. 
