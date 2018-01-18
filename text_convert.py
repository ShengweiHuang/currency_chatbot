import jieba
import currency as curr

input_error_return = "我們提供外幣金額轉換的服務，請您輸入以下資料，我們將會為您查詢即時資訊\n1. 幣別種類\n2. 該幣別金額\n3. 買入或賣出(可不填)\n4. 現金或期貨(可不填)"

def get_output_str(input_str = ""):
	input_list = (list)(jieba.cut(input_str))
	# get data from list
	currency_id = get_currency_type(input_list)
	quantity = get_quantity(input_list)
	buy_or_sell = get_buy_or_sell(input_list)
	cash_or_spot = get_cash_or_spot(input_list)
	# get currency data
	if currency_id == -1 or currency_id == 0:
		return input_error_return
	new_data = curr.convert_to_TWD(currency_id, quantity)
	# generate result
	result_str = ""
	if buy_or_sell != -1 and cash_or_spot != -1:
		result_str += "換算新台幣約: " + str(new_data[2 * buy_or_sell + cash_or_spot]) + "元"
	if buy_or_sell == -1 and cash_or_spot != -1:
		result_str += "銀行買入換算新台幣約: " + str(new_data[cash_or_spot]) + "元\n"
		result_str += "銀行賣出換算新台幣約: " + str(new_data[cash_or_spot + 2]) + "元\n"
	if buy_or_sell != -1 and cash_or_spot == -1:
		result_str += "現金匯率換算新台幣約: " + str(new_data[2 * buy_or_sell]) + "元\n"
		result_str += "即期匯率換算新台幣約: " + str(new_data[2 * buy_or_sell + 1]) + "元\n"
	if buy_or_sell == -1 and cash_or_spot == -1:
		result_str += "現金銀行買入換算新台幣約: " + str(new_data[0]) + "元\n"
		result_str += "即期銀行買入換算新台幣約: " + str(new_data[1]) + "元\n"
		result_str += "現金銀行賣出換算新台幣約: " + str(new_data[2]) + "元\n"
		result_str += "即期銀行賣出換算新台幣約: " + str(new_data[3]) + "元"
	return result_str
	
def get_currency_type(input_list):
	with open("currency_name.txt", 'r') as name_file:
		namelist = name_file.readlines()
	for i in input_list:
		for j in range(1, len(namelist)):
			if i in namelist[j]:
				return j
	return -1 

def get_quantity(input_list):
	quantity = 0
	for i in input_list:
		try:
			quantity = int(i)
			return quantity
		except:
			pass
	return 1

def get_buy_or_sell(input_list):
	# buy -> 0, sell -> 1, none of all -> -1
	for i in input_list:
		if "賣" in i:
			return 0
		if "買" in i:
			return 1
	return -1

def get_cash_or_spot(input_list):
	# cash -> 0, spot -> 1, none of all -> -1
	for i in input_list:
		if "現金" in i:
			return 0
		if "即期" in i:
			return 1
	return -1

if __name__ == "__main__":
	print(get_output_str(input(">")))
