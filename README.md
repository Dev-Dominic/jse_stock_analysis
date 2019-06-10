# Jamaica Stock Exchange Analysis 

The purpose of this project is to extract the csv files of a given time period from the JSE website and to make relevant calculations on the data retrieved. Calculations such as the percantage gain on each stock, as well as, the dollar gain on each stock in a given time period. 

## Project File Structure
 
```bash

jse_stock_analysis
├── main.py
├── scripts
│   ├── data_process.py
│   ├── data_pull.py
│   └── web_scrape.py
└── * temp

```

### main.py

This script is where the main method is ran from, on the command line run 

```bash

$ main.py 'start_date' 'end_date'
$ main.py 20-12-2011 20-12-2018

```

### scripts

#### web_scrape.py

This script will retrieve all the csv files from the JSE website based on the passed dates to the main.py script.Storing all the csv files in temp.

#### data_pull.py

This script will pull all the data from the csv files and storing each stock's data in a suitable data structure.

#### data_process.py
 
This script will make the relevant calcuations on the data received from the data_ull.py script and then passing it to the main.py script to display the information.
