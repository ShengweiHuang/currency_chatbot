import jieba

input_error_return = "我們提供外幣金額轉換的服務，請輸入您輸入以下資料，我們將會為您查詢即時資訊\n1. 幣別種類\n2. 該幣別金額\n3. 買入或賣出(可不填)\n4. 現金或期貨(可不填)"
buy = ["買入", "買進", "買"]
sell = []

def get_output_str(input_str = ""):
	return input_error_return

def get_data(input_str = ""):
	input_list = (list)(jieba.cut(input_str))
	

if __name__ == "__main__":
	get_output_str()
