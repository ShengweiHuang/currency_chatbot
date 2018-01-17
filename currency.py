import csv
import urllib.request
import os

CURRENCY_URL = "http://rate.bot.com.tw/xrt/flcsv/0/day"
CURRENCY_FILE_NAME = "currency_data.csv"

def get_currency_data():
	currency_list = []
	urllib.request.urlretrieve(CURRENCY_URL, CURRENCY_FILE_NAME)
	with open(CURRENCY_FILE_NAME, "r") as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
		for row in spamreader:
			return_list.append(row)
	os.remove(CURRENCY_FILE_NAME)
	return currency_list

def get_currency_id(currency_type):
	currency_data = get_currency_data()
	

if __name__ == "__main__":
	get_currency_data()
