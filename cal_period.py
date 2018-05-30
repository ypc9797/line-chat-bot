import datetime
import google_sheet
from datetime import datetime, timedelta,date

def next_period(user_id,choice):
	the_id = user_id

	auth_json_path = 'google_sheet.json'
	gss_scopes = ['https://spreadsheets.google.com/feeds']
	gss_client = google_sheet.auth_gss_client(auth_json_path, gss_scopes)
	spreadsheet_key = '1Q4hWEVjTB-rdc7HAi_Yc_cF4uymjfPHe70Cc36fLHyM'
	print("我是五")
	try:
		print('im here!!')
		last_date_str = google_sheet.find_user_period(gss_client, spreadsheet_key, the_id)
		print(last_date_str)
	except:
		print("我是六")
		return 0

	last_date = datetime.strptime(last_date_str,"%Y-%m-%d")	
	period = last_date + timedelta(days=28) #月經日期是第一天加上週期
	preg = last_date + timedelta(days=10) #經期來後10天開始的一周內容易懷孕
	diet = last_date + timedelta(days=7) #經期來後7天開始的一周內容易懷孕
	bra = last_date + timedelta(days=17)

	profile = line_bot_api.get_profile(the_id)
	user_name = profile.display_name

	if choice == 'all' :
		content = ''
		content += user_name + ' 你好~'
		content += '已成功紀錄你最近來的日期' + event.postback.params['date'] + '\n\n'
		content += '預計下一次差不多會是' + period.strftime("%m/%d") + '來\n\n'
		content += preg.strftime("%m/%d") + ' 開始的一週很容易懷孕 (╯°Д°)╯ ┻━┻\n\n'
		content += diet.strftime("%m/%d") + ' 開始的一週內少吃多動會瘦很快!!\n\n'
		content += bra.strftime("%m/%d") + ' 開始的一週多按摩奶奶會長很大唷\n\n'
		content += '輸入"科普"來補充更多小知識吧 (✿╹◡╹)'

	return content