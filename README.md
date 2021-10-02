# Python Challenge - Py Me Up, Charlie

## Background

Welcome to the world of programming with Python. In this assignment, I am applying the Python concepts to complete the **two** Python Challenges tasks: PyBank and PyPoll.


# Steps

* Inside this Python Challenge repository, there are two fodlers: **PyBank** and **PyPoll**.

* Inside of each folder, there are following information:

  * A file called `main.py`. This will be the main script to run for each analysis.
  
  * A "Resources" folder that contains the raw data in CSV format. 
  
  * An "Analysis" folder that contains the text file with the results from the analysis.


## Task I: PyBank Budget Analysis

* In this challenge, I am creating a Python script for analyzing the financial records of a small company. The set of financial data called `budget_data.csv` is stored in the [Resources] folder. The dataset is composed of two columns: `Date` and `Profit/Losses`. 

* My Python script analyzes the bueget records to calculate the following information:

  * The total number of months included in the dataset;

  * The net total amount of "Profit/Losses" shows the Net changes over the entire period;

  * The total differences of the monthly changes in "Profit/Losses" over the entire period, 
    and calculate the average of those differences;

  * The greatest increase in profits (date and amount) over the entire period;

  * The greatest decrease in profits (date and amount) over the entire period;
  
  * Below is the format of my scrpit that will be printed to the Termianl::

    ```text
    Financial Analysis
    ---------------------------------------------------
    Total Months: 86
    Total: $38382578
    Average  Change: $-2315.12
    Greatest Increase in Profits: Feb-2012 ($1926159)
    Greatest Decrease in Profits: Sep-2013 ($-2196167)
    ---------------------------------------------------
    ```

  * In addition, the final script will be exported as a text file with the results.



## Task II: PyPoll Election Result

* In this challenge, I am tasked with helping a small, rural town modernize its vote counting process.  The set of poll data called `election_data.csv` is stored in the [Resources] folder. The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 

* My Python script analyzes the vote records to calculate the election result that includes the following infirmation:

  * The total number of votes cast;

  * A complete list of candidates who received votes;

  * The percentage of votes each candidate won;

  * The total number of votes each candidate won;

  * The winner of the election based on popular vote;

  * Below is the format of my scrpit that will be printed to the Termianl::

    ```text
    Election Results
    -------------------------
    Total Votes: 3521001
    -------------------------
    Khan: 63.000% (2218231)
    Correy: 20.000% (704200)
    Li: 14.000% (492940)
    O'Tooley: 3.000% (105630)
    -------------------------
    Winner: Khan
    -------------------------
    ```

  * In addition, the final script will be exported as a text file with the results.
