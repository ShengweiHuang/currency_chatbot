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
			currency_list.append(row)
	os.remove(CURRENCY_FILE_NAME)
	return currency_list

def convert_to_TWD(currency_id, quantity, trading_type = -1, currency_data = get_currency_data()):
	# buying cash, buying spot, selling cash, selling spot
	data_row = currency_data[currency_id]
	return_data = [float(data_row[2]), float(data_row[3]), float(data_row[12]),float(data_row[13])]
	return_data = [i * quantity for i in return_data]
	if trading_type == -1:
		return return_data
	else:
		return return_data[trading_type]

def convert_from_TWD(quantity, currency_id = -1, trading_type = -1, currency_data = get_currency_data()):
	# if currency_id == -1, list all currency
	if currency_id == -1:
		return_data = []
		data_row = currency_data[1:]
		for i in range(1, len(currency_data)):
			data_row = currency_data[i]
			return_data_row = [float(data_row[2]), float(data_row[3]), float(data_row[12]),float(data_row[13])]
			return_data_row = [(0 if j == 0 else quantity / j) for j in return_data_row]
			return_data.append(return_data_row)
	else:
		data_row = currency_data[currency_id]
		return_data = [float(data_row[2]), float(data_row[3]), float(data_row[12]),float(data_row[13])]
		return_data = [(quantity / i) for i in return_data]
	if trading_type != -1:
		if currency_id == -1:
			return_data = [i[trading_type] for i in return_data]
		else:
			return_data = return_data[trading_type]
	return return_data

def get_currency_id(currency_type, currency_data = get_currency_data()):
	for i in range(0, len(currency_data)):
		if currency_data[i][0] == currency_type:
			return i
	return -1

if __name__ == "__main__":
	get_currency_data()
