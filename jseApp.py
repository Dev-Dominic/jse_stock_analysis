"""
    This python script is used to pull csvfile stock data from the Jamaica Stock exchange website
    and process the data to produce data to analyze the strength of stocks on the exchange.

"""

# Imports
import os
import sys
from bs4 import BeautifulSoup
from csv import DictReader
from urllib import request
import lxml
import datetime
from time import sleep
    
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
        for i in range(3):
            try:
                # Making request to JSE market-quote page to junior market index 
                jse_request = request.urlopen('https://www.jamstockex.com/market-data/junior-market/quote/' + dateStr) 
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


# Main
if __name__ == "__main__":
    # Creates an empty dictionary to hold all stock data 
    stock_list = dict() 

    # Retrieves csv files from JSE website
    retrieve_csv_files("2019-01-31", "2019-06-30")

    # Pulls Stock name and Close Prices from csv files and places into stock_list



