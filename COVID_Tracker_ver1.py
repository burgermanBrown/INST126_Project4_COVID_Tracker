import pandas as pd
import matplotlib.pyplot as plt

county_data = pd.read_csv("us-counties.csv")
state_data = pd.read_csv("us-states.csv")

#covid_deaths, cases use the same functions (sort, range, display) but will pass different arguments
def covid_deaths():
  print("hello0")
  #displays data on covid deaths by state or county
def covid_cases():
  print("hello1")
  #displays data on covid deaths by state or county
def set_range():
  print("hello2")
  #set the range for matplot graphs via user input
def display(df):
  print("hello3")
  #takes values from set_range() and plots them visually using desired format (histogram, pie chart, etc)

selection = input("Please enter a function: Covid Deaths, Covid Cases")
selection = selection.lower()
if selection == 'deaths':
  covid_deaths()
elif selection == 'cases':
  covid_cases()
else:
  print("Invalid Selection")