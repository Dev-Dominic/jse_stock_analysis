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

    
def retrieve_csv_files(st_date, st_end):
    # Creating Temporary directory 'temp' to store csv files
    os.mkdir('temp')

    # Loops through start day quote page to end date quote page
    

    # Making request to JSE market-quote page to junior market index
    jse_request = request.urlopen('https://www.jamstockex.com/market-data/junior-market/quote/' + st_date)
    soup = BeautifulSoup(jse_request, "lxml")

    # CSV donwloads tag
    download_link = soup.find_all("a", class_="btn btn-primary")

    print(download_link[1].attrs['href'])
    fileData = request.urlopen(download_link[1].attrs['href'])
    dataFile = fileData.read()

    with open('stock1.csv', 'wb') as f:
        f.write(dataFile)

    print(dataFile)

# Main
if __name__ == "__main__":
    # Creates an empty dictionary to hold all stock data 
    stock_list = dict() 
    retrieve_csv_files("2019-06-10", "2019-06-16")


