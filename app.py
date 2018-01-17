from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os
import csv

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['LINEBOT_CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['LINEBOT_CHANNEL_SECRET'])

CURRENCY_URL = "http://rate.bot.com.tw/xrt/flcsv/0/day"
CURRENCY_FILE_NAME = "currency_data.csv"

@app.route("/callback", methods=['POST'])
def callback():
	# get X-Line-Signature header value
	signature = request.headers['X-Line-Signature']
	# get request body as text
	body = request.get_data(as_text=True)
	print("Request body: " + body, "Signature: " + signature)
	# handle webhook body
	try:
		handler.handle(body, signature)
	except InvalidSignatureError:
		abort(400)
	return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	print("Handle: reply_token: " + event.reply_token + ", message: " + event.message.text)
	#content = event.message.text
	content = get_currency_data()
	line_bot_api.reply_message(event.reply_token, TextSendMessage(text=content))

def get_currency_data():
	return_str = ""
	os.system("wget -O " + CURRENCY_FILE_NAME + " " + CURRENCY_URL)
	with open(CURRENCY_FILE_NAME, "rb") as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar=',')
		for row in spamreader:
			return_str += ', '.join(row) + "\n"
	os.remove(CURRENCY_FILE_NAME)
	return return_str

if __name__ == "__main__":
	app.run(host=os.getenv('IP','0.0.0.0'), port=int(os.getenv('PORT','8080')))
