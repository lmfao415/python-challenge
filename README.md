# python-challenge

This repository contains two small projects involving Python analysis of two datasets provided in CSV format. 

* The first [PyBank](https://github.com/lmfao415/python-challenge/tree/main/PyBank) analysis 
reads the financial data listed in [budget_data.csv](https://github.com/lmfao415/python-challenge/blob/main/PyBank/Resources/budget_data.csv) and returns the [analysis](https://github.com/lmfao415/python-challenge/blob/main/PyBank/analysis/budget_analysis) text file. The financial data here is provided as a table of profits/losses per month over about seven years. 

  Running the [main.py](https://github.com/lmfao415/python-challenge/blob/main/PyBank/main.py) file analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

  Here are the results as printed to the [budget_analysis](https://github.com/lmfao415/python-challenge/blob/main/PyBank/analysis/budget_analysis) text file
![Here are the results](https://github.com/lmfao415/python-challenge/blob/main/PyBank/analysis/analysis.png?raw=true)


* The second [PyPoll](https://github.com/lmfao415/python-challenge/tree/main/PyPoll) analysis takes a look vote data from an election found in [election_data.csv](https://github.com/lmfao415/python-challenge/blob/main/PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 

  Running the [main.py](https://github.com/lmfao415/python-challenge/blob/main/PyPoll/main.py) file analyzes the votes and calculates the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.
  
  Here are the results as printed to the [election_results](https://github.com/lmfao415/python-challenge/blob/main/PyPoll/analysis/election_results) text file
![Here are the results](https://github.com/lmfao415/python-challenge/blob/main/PyPoll/analysis/analysis.png?raw=true)
  
