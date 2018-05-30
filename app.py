import sys

import datetime

import google_sheet

from flask import Flask, request, abort
from datetime import datetime, timedelta,date
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage,SourceUser,
	TemplateSendMessage, ButtonsTemplate,PostbackEvent,
    PostbackTemplateAction, MessageTemplateAction,MessageImagemapAction,
    URITemplateAction, DatetimePickerTemplateAction,
    ConfirmTemplate, CarouselTemplate, CarouselColumn,
    ImageCarouselTemplate, ImageCarouselColumn, VideoSendMessage,BaseSize
)


app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('1weJtNcy1GERLrg3CrgBYGxQPee7u7uZ8DEfjYiHBdzP2IFai3JB5HRATY8+ziuYUX1ZBrdbQNqaRSQlWivFPhL9hXlqTbOL8sT9rEW+ld6yalG1m7KQf1M/qMMRHbBqCJ0Bv7o+nL5ak6uyDXkAJwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('77488403fcfe053c2220351cdeba4e56')


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

	if event.message.text == '第一次':
		image_carousel_template = ImageCarouselTemplate(columns=[
			ImageCarouselColumn(image_url='https://upload.cc/i1/2018/05/28/bLum7a.png',
								action=DatetimePickerTemplateAction(label='點我選最近一次經期日期',
																	data='first',
																	mode='date'))
			])
		template_message = TemplateSendMessage(
		alt_text='第一次輸入月經', template = image_carousel_template)
		line_bot_api.reply_message(event.reply_token, template_message)
		return 0

	elif event.message.text in ('算一下','查詢'):
		image_carousel_template = ImageCarouselTemplate(columns=[
			ImageCarouselColumn(image_url='https://upload.cc/i1/2018/05/28/bLum7a.png',
								action=DatetimePickerTemplateAction(label='查一下好日子',
																	data='cal'
																	))
			])
		template_message = TemplateSendMessage(
		alt_text='算一下良辰吉時', template = image_carousel_template)
		line_bot_api.reply_message(event.reply_token, template_message)
		return 0

	elif event.message.text in ('hi','Hi','HI','hello','你好','哈囉','嗨'):
		profile = line_bot_api.get_profile(event.source.user_id)
		line_bot_api.reply_message(
			event.reply_token, [
				TextSendMessage(
					text='Hi hi ' + profile.display_name
				)
			]
		)		

	elif event.message.text == 'id':
		line_bot_api.reply_message(
			event.reply_token, [
				TextSendMessage(
					text='id: ' + event.source.user_id
				)
			]
		)
			
	elif event.message.text == '瘦腿':
		line_bot_api.reply_message(
			event.reply_token,[
				TextSendMessage(text='https://www.youtube.com/watch?v=3X1PL7ym04I&list=PL2T5-4ENPUpIkpC0oGj6r-dLLluOeSeUn&index=2&t=1s'),
				TextSendMessage(text='https://www.youtube.com/watch?v=Rr8CEyQ3-5k&index=2&list=PL2T5-4ENPUpIkpC0oGj6r-dLLluOeSeUn')
			])
		return 0
		
	elif event.message.text == '蝴蝶袖':
		line_bot_api.reply_message(
			event.reply_token,[
				TextSendMessage(text='https://www.youtube.com/watch?v=C8oSs8qf_7g'),
				TextSendMessage(text='https://www.youtube.com/watch?v=Fh0WLIFQVdk')
			])
		return 0
		
	elif event.message.text == '瘦肚子':
		line_bot_api.reply_message(
			event.reply_token,[
				TextSendMessage(text='https://www.youtube.com/watch?v=dzFs1eA6DV8'),
				TextSendMessage(text='https://www.youtube.com/watch?v=qT9aYCk5fmI')
			])
		return 0
		
	elif event.message.text == '激烈一點':
		line_bot_api.reply_message(
			event.reply_token,[
				TextSendMessage(text='https://www.youtube.com/watch?v=40Gd7pOF0L8'),
				TextSendMessage(text='https://www.youtube.com/watch?v=ByLnybm0M88')
			])
		return 0
	
	elif event.message.text in ('豐胸運動', '豐胸'):
		line_bot_api.reply_message(
			event.reply_token,[
				TextSendMessage(text='https://www.youtube.com/watch?v=eBcZ22nUV_k'),
				TextSendMessage(text='https://www.youtube.com/watch?v=2HfEp3fpO9I')
			])
		return 0

	elif event.message.text in ('那個來'):
		message = TextSendMessage(text='那個來怎麼辦呢')
		line_bot_api.reply_message(event.reply_token, message)
	elif event.message.text in ('沒來'):
		message = TextSendMessage(text='沒來怎麼辦呢')
		line_bot_api.reply_message(event.reply_token, message)
	elif event.message.text in ('避孕'):
		message = TextSendMessage(text='怎麼避孕呢')
		line_bot_api.reply_message(event.reply_token, message)
		
	elif event.message.text in ('睡前瘦身', '減肥'):
		buttons_template = TemplateSendMessage(
			alt_text='睡前瘦身 template',
			template=ButtonsTemplate(
				title='想瘦哪兒',
				text='請選擇',
				thumbnail_image_url='https://upload.cc/i1/2018/05/27/9bakSs.png',
				actions=[
					MessageTemplateAction(
						label='瘦腿',
						text='瘦腿'
					),
					MessageTemplateAction(
						label='蝴蝶袖',
						text='蝴蝶袖'
					),
					MessageTemplateAction(
						label='瘦肚子',
						text='瘦肚子'
					),
					MessageTemplateAction(
						label='激烈一點',
						text='激烈一點'
					)
				]
			)
		)
		line_bot_api.reply_message(event.reply_token, buttons_template)
		return 0

	elif event.message.text in ('看帥哥', '看猛男'):	
		message = TemplateSendMessage(
			alt_text='menu template',
			template=ImageCarouselTemplate(
				columns=[
					ImageCarouselColumn(
						image_url='https://upload.cc/i1/2018/05/28/0BqKvb.png',
						action=MessageTemplateAction(
							label='減肥',
							text='減肥',
						)
					),
					ImageCarouselColumn(
						image_url='https://upload.cc/i1/2018/05/27/cm2Gua.png',
						action=MessageTemplateAction(
							label='豐胸',
							text='豐胸',
						)
					),
					ImageCarouselColumn(
						image_url='https://upload.cc/i1/2018/05/27/rMB73X.png',
						action=MessageTemplateAction(
							label='減肥',
							text='減肥',
						)
					),
					ImageCarouselColumn(
						image_url='https://upload.cc/i1/2018/05/27/O0VTrv.png',
						action=MessageTemplateAction(
							label='豐胸',
							text='豐胸',
						)
					),
					ImageCarouselColumn(
						image_url='https://upload.cc/i1/2018/05/27/onFG3Y.png',
						action=MessageTemplateAction(
							label='減肥',
							text='減肥',
						)
					)
				]
			)
		)
		line_bot_api.reply_message(event.reply_token, message)
		return 0

	elif event.message.text in ('科普', '知識'):	
		message = TemplateSendMessage(
			alt_text='knownledge template',
			template=ImageCarouselTemplate(
				columns=[
					ImageCarouselColumn(
						image_url='https://upload.cc/i1/2018/05/28/hayQre.png',
						action=MessageTemplateAction(
							label='那個來',
							text='那個來',
						)
					),
					ImageCarouselColumn(
						image_url='https://upload.cc/i1/2018/05/28/7czXVi.png',
						action=MessageTemplateAction(
							label='沒來',
							text='沒來',
						)
					),
					ImageCarouselColumn(
						image_url='https://upload.cc/i1/2018/05/28/lU1ftP.png',
						action=MessageTemplateAction(
							label='避孕',
							text='避孕',
						)
					)
				]
			)
		)
		line_bot_api.reply_message(event.reply_token, message)
		return 0

	elif event.message.text in ('看正妹', '看美女'):	
		message = TemplateSendMessage(
			alt_text='menu template',
			template=ImageCarouselTemplate(
				columns=[
					ImageCarouselColumn(
						image_url='https://upload.cc/i1/2018/05/27/ZzRxic.png',
						action=MessageTemplateAction(
							label='豐胸',
							text='豐胸',
						)
					),
					ImageCarouselColumn(
						image_url='https://upload.cc/i1/2018/05/27/1A0gEe.png',
						action=MessageTemplateAction(
							label='減肥',
							text='減肥',
						)
					),
					ImageCarouselColumn(
						image_url='https://upload.cc/i1/2018/05/27/XrYx1e.png',
						action=MessageTemplateAction(
							label='減肥',
							text='減肥',
						)
					),
					ImageCarouselColumn(
						image_url='https://upload.cc/i1/2018/05/27/ltEiag.png',
						action=MessageTemplateAction(
							label='豐胸',
							text='豐胸',
						)
					),
					ImageCarouselColumn(
						image_url='https://upload.cc/i1/2018/05/27/3YHWAq.png',
						action=MessageTemplateAction(
							label='減肥',
							text='減肥',
						)
					)
				]
			)
		)
		line_bot_api.reply_message(event.reply_token, message)
		return 0
		
	elif event.message.text in ('激勵', '看圖'):
		message = TemplateSendMessage(
			alt_text='Confirm template',
			template=ConfirmTemplate(
				text='看看別人，勉勵自己。來帖帥哥還是正妹？',
				actions=[
					MessageTemplateAction(
						label='看帥哥',
						text='看帥哥',
					),
					MessageTemplateAction(
						label='看美女',
						text='看美女'
					)
				]
			)
		)
		line_bot_api.reply_message(event.reply_token, message)  
		return 0
	
	elif event.message.text in ('menu','Menu','目錄','姨媽'):
		message = TemplateSendMessage(
			alt_text='menu template',
			template=ImageCarouselTemplate(
				columns=[
					ImageCarouselColumn(
						image_url='https://upload.cc/i1/2018/05/27/hVyS0H.png',
						action=MessageTemplateAction(
							label='算一下日期',
							text='算一下',
						)
					),
					ImageCarouselColumn(
						image_url='https://upload.cc/i1/2018/05/27/kiDedJ.png',
						action=MessageTemplateAction(
							label='減肥',
							text='減肥',
						)
					),
					ImageCarouselColumn(
						image_url='https://upload.cc/i1/2018/05/27/E96QJF.png',
						action=MessageTemplateAction(
							label='豐胸',
							text='豐胸',
						)
					),
					ImageCarouselColumn(
						image_url='https://upload.cc/i1/2018/05/28/efM7Sc.png',
						action=MessageTemplateAction(
							label='激勵',
							text='激勵',
						)
					),
					ImageCarouselColumn(
						image_url='https://upload.cc/i1/2018/05/28/YfSntk.png',
						action=MessageTemplateAction(
							label='科普',
							text='科普',
						)
					),
					ImageCarouselColumn(
						image_url='https://upload.cc/i1/2018/05/28/knXNB3.png',
						action=PostbackTemplateAction(
							Label='聯絡姨媽',
							text='聯絡姨媽',
							data='contact_me',
						)
					)
				]
			)
		)
		line_bot_api.reply_message(event.reply_token, message)
		return 0

	elif event.message.text in ('聯絡姨媽','姨媽是誰','找姨媽'):
		message = TemplateSendMessage(
			alt_text='姨媽的聯絡方式',
			template=ButtonsTemplate(
				thumbnail_image_url='https://upload.cc/i1/2018/05/28/Qtp3hR.png',
				title='這裡找姨媽',
				text='喜歡請按讚',
				actions=[
		            URITemplateAction(
		                label='Facebook',
		                uri='https://www.facebook.com/anna.yaping'
		            ),
		            URITemplateAction(
		                label='Instagram',
		                uri='https://www.instagram.com/anna_yaping/'
		            )
		 		]
			)
		)
		line_bot_api.reply_message(event.reply_token, message)		

	else :
		message = TextSendMessage(text=event.message.text)
		line_bot_api.reply_message(event.reply_token, message)



@handler.add(PostbackEvent)
def handle_postback(event):
	if event.postback.data == 'first':
		the_day = event.postback.params['date']
		last_date = datetime.strptime(the_day,"%Y-%m-%d")
		period = last_date + timedelta(days=28) #月經日期是第一天加上週期
		preg = last_date + timedelta(days=10) #經期來後10天開始的一周內容易懷孕
		diet = last_date + timedelta(days=7) #經期來後7天開始的一周內容易懷孕
		bra = last_date + timedelta(days=17)

		the_id = event.source.user_id
		profile = line_bot_api.get_profile(the_id)
		user_name = profile.display_name

		content = ''
		content += user_name + ' 你好~'
		content += '已成功紀錄你最近來的日期' + event.postback.params['date'] + '\n\n'
		content += '預計下一次差不多會是' + period.strftime("%m/%d") + '來\n\n'
		content += preg.strftime("%m/%d") + ' 開始的一週很容易懷孕 (╯°Д°)╯ ┻━┻\n\n'
		content += diet.strftime("%m/%d") + ' 開始的一週內少吃多動會瘦很快!!\n\n'
		content += bra.strftime("%m/%d") + ' 開始的一週多按摩奶奶會長很大唷\n\n'
		content += '輸入"科普"來補充更多小知識吧 (✿╹◡╹)'



		auth_json_path = 'google_sheet.json'
		gss_scopes = ['https://spreadsheets.google.com/feeds']
		gss_client = google_sheet.auth_gss_client(auth_json_path, gss_scopes)
		spreadsheet_key = '1Q4hWEVjTB-rdc7HAi_Yc_cF4uymjfPHe70Cc36fLHyM'

		google_sheet.update_sheet(gss_client, spreadsheet_key, the_id, the_day)
		line_bot_api.reply_message(event.reply_token, TextSendMessage(text=content))


	elif event.postback.data == 'cal':
		the_id = event.source.user_id
		profile = line_bot_api.get_profile(the_id)
		user_name = profile.display_name
		
		auth_json_path = 'google_sheet.json'
		gss_scopes = ['https://spreadsheets.google.com/feeds']
		gss_client = google_sheet.auth_gss_client(auth_json_path, gss_scopes)
		spreadsheet_key = '1Q4hWEVjTB-rdc7HAi_Yc_cF4uymjfPHe70Cc36fLHyM'

		try:
			print('im here!!')
			last_date_str = find_user_period(gss_client, spreadsheet_key, the_id)
			print(last_date_str)
		except:
			line_bot_api.reply_message(event.reply_token, TextSendMessage(text='你還沒有輸入最近的一次月經日期歐～請輸入"第一次"來選擇吧!!'))
		
		last_date = datetime.strftime(last_date_str,"%Y-%m-%d")		
		period = last_date + timedelta(days=28) #月經日期是第一天加上週期
		preg = last_date + timedelta(days=10) #經期來後10天開始的一周內容易懷孕
		diet = last_date + timedelta(days=7) #經期來後7天開始的一周內容易懷孕
		bra = last_date + timedelta(days=17)

		content = ''
		content += user_name + ' 你好~\n'
		content += '你上次紀錄的日期是' + last_date_str + '\n\n'
		content += '預計下一次差不多會是' + period.strftime("%m/%d") + '來\n\n'
		content += preg.strftime("%m/%d") + ' 開始的一週很容易懷孕 (╯°Д°)╯ ┻━┻\n\n'
		content += diet.strftime("%m/%d") + ' 開始的一週內少吃多動會瘦很快!!\n\n'
		content += bra.strftime("%m/%d") + ' 開始的一週多按摩奶奶會長很大唷\n\n'
		content += '輸入"科普"來補充更多小知識吧 (✿╹◡╹)'
		line_bot_api.reply_message(event.reply_token, TextSendMessage(text=content))


	elif event.postback.data == 'contact_me':
		line_bot_api.reply_message(event.reply_token, TextSendMessage(text='找我嗎(〃▽〃)?'))

			

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
