from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os
import text_convert as tc

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['LINEBOT_CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['LINEBOT_CHANNEL_SECRET'])

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
	content = tc.get_output_str(event.message.text)
	line_bot_api.reply_message(event.reply_token, TextSendMessage(text=content))

if __name__ == "__main__":
	app.run(host=os.getenv('IP','0.0.0.0'), port=int(os.getenv('PORT','8080')))
