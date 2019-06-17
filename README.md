# Jamaica Stock Exchange Analysis 

The purpose of this project is to extract the csv files of a given time period from the JSE website and to make relevant calculations on the data retrieved. Calculations such as the percantage gain on each stock, as well as, the dollar gain on each stock in a given time period. 

### jseApp.py

The main method and all the supporting functions are containted in `jseApp.py`
The command line arguments passed are the start date and end date for which the data should be searched within and inclusive of.

```bash

$ jseApp.py 'start_date' 'end_date'
$ jseApp.py 20-12-2011 20-12-2018

```

### Core functions 

1. Web Scrape JSE website
2. Create a temproray folder to house csvfiles
3. Download all csv files from start date to end state (inclusive)
4. Store all the stock's data in a list
5. Perform calculations on each stock's data
6. Presetaton of information that was processed
