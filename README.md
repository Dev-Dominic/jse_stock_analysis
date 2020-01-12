# Jamaica Stock Exchange Analysis v1.0

The purpose of this project is to extract the csv files of a given time period from the JSE website and to make relevant calculations on the data retrieved. Calculations such as the percantage gain on each stock, as well as, the dollar gain on each stock in a given time period. 


## Installation and Setup

### Requirements
1. Python 3
2. Pip

### Installing pipenv and getting repo
```bash

$ pip install pipenv 
$ git clone https://github.com/Dev-Dominic/jse_stock_analysis.git

```

Navigate in terminal/command line to location of project folder

### Setting up pipenv 

Note: Ensure you perform commands in project folder 

```bash

$ pipenv shell
$ pipenv install 

```

This should successfully install all the dependencies for the script

## Closing pipenv virutal environment

```bash

$ exit

```

Close virtual enviroment after finishing use of the script and project

### jseApp.py

The main method and all the supporting functions are containted in `jseApp.py`
The command line arguments passed are the start date and end date for which the data should be searched within and inclusive of.

```bash

$ python jseApp.py 'start_date' 'end_date'
$ python jseApp.py 2011-12-20	2018-12-20 <year-month-day>

```

### Core functions 

1. Web Scrape JSE website
2. Create a temproray folder to house csvfiles
3. Download all csv files from start date to end state (inclusive)
4. Store all the stock's data in a list
5. Find out the average closing stock price of each security
6. Presetaton of information that was processed
