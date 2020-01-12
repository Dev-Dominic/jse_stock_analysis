"""
    This python script is used to pull csvfile stock data from the Jamaica Stock exchange website
    and process the data to produce data to analyze the strength of stocks on the exchange.

"""

# Imports
import os
import sys
from bs4 import BeautifulSoup
import csv
from urllib import request
import lxml
import datetime
from time import sleep
from statistics import mean
    
def retrieve_csv_files(st_date, end_date):
    # Creating Temporary directory 'temp' to store csv files
    os.mkdir('temp')

    # Loops through start day quote page to end date quote page
    dateStartObj = datetime.datetime.strptime(st_date, "%Y-%m-%d")
    dateEndObj = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    
    while dateStartObj <= dateEndObj:
        # Datetime string object for date
        dateStr = dateStartObj.strftime("%Y-%m-%d")

        print(dateStr)

        # Makes request to JSE three times for a page before throwing exception
        for i in range(4):
            try:
                # Making request to JSE market-quote page to junior market index 
                jse_request = request.urlopen('https://www.jamstockex.com/market-data/combined-market/quote/' + dateStr) 
                soup = BeautifulSoup(jse_request, "lxml") 
                
                # CSV donwloads tag 
                download_link = soup.find_all("a", class_="btn btn-primary") 
                fileData = request.urlopen(download_link[1].attrs['href']) 
                
                with open('temp/' +dateStr +'.csv', 'wb') as f: 
                    f.write(fileData.read())

                # Increments start date
                dateStartObj += datetime.timedelta(days=1)

                # Goes to sleep so as to not make many requests to the JSE website to timeout
                sleep(1)

                break
            except:
                continue

# Pulls the stock name and closed price for each day and retuns as a dictionary
def pullStockData(st_date, end_date):
    stock_list = dict()

    dateStartObj = datetime.datetime.strptime(st_date, "%Y-%m-%d")
    dateEndObj = datetime.datetime.strptime(end_date, "%Y-%m-%d")

    while dateStartObj <= dateEndObj:
        dateStr = dateStartObj.strftime("%Y-%m-%d")

        with open('temp/' + dateStr + '.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if(row != []):
                    if(row[0] not in ['Security', 'Preference Shares', 'Index Data', 'Index', 'JSE-Junior', 'Ordinary Shares']):
                        if(row[0] not in stock_list):
                            stock_list[row[0]] = [float(row[2])] 
                        else:
                            stock_list[row[0]].append(float(row[2]))

        dateStartObj += datetime.timedelta(days=1)

    return stock_list 

# Takes a dictionary containing stock name and close prices 
# Returns a list of tuples with (Stock Tag, Net Change)
# def processData(stock_list):
    # return [(keys,float("{0:.2f}".format(values[-1]-values[0]))) for keys, values in stock_list.items()]

# Filters out stocks that had and average stock price less than or equal to filter_price
def filterStocks(stock_list, filter_price):
    stockAvg = [(keys, float("{0:.2f}".format(mean(values)))) for keys, values in stock_list.items()]
    return filter(lambda stock: stock[1] <= filter_price, stockAvg) 

# Deletes temp folder and all csv files
def garbageCollection():
    os.chdir("temp")
    
    # Deleting all files
    for tempFile in os.listdir():
        os.remove(tempFile)

    os.chdir("..")
    os.rmdir("temp")

# TODO Implement proper command-line options 
"""
    Main 
    $ python jseApp.py <start-date> <end-date> <filter-price> 

    Gets a stock based on the average price from <start-date> and <end-date> 
    were all the stocks with averages that are less than or equal to the filter-price is returned

"""
if __name__ == "__main__":
    # Retrieves csv files from JSE website
    retrieve_csv_files(sys.argv[1], sys.argv[2])

    # Pulls Stock name and Close Prices from csv files and places into stock_list
    stock_list = pullStockData(sys.argv[1], sys.argv[2])
    # stock_info_list = processData(stock_list)

    filter_price = float(sys.argv[3])
    stock_info_list = filterStocks(stock_list, filter_price)

    for i in stock_info_list:
        print(i)

    garbageCollection()
