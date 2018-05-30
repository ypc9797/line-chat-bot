import datetime
import google_sheet
from datetime import datetime, timedelta,date


def next_period(user_id,username,choice):
	the_id = user_id
	user_name = username
	auth_json_path = 'google_sheet.json'
	gss_scopes = ['https://spreadsheets.google.com/feeds']
	gss_client = google_sheet.auth_gss_client(auth_json_path, gss_scopes)
	spreadsheet_key = '1Q4hWEVjTB-rdc7HAi_Yc_cF4uymjfPHe70Cc36fLHyM'
	last_date_str = google_sheet.find_user_period(gss_client, spreadsheet_key, the_id)
	if last_date_str ==0:
		return 0

	last_date = datetime.strptime(last_date_str,"%Y-%m-%d")	
	period = last_date + timedelta(days=28) #月經日期是第一天加上週期
	preg = last_date + timedelta(days=10) #經期來後10天開始的一周內容易懷孕
	diet = last_date + timedelta(days=7) #經期來後7天開始的一周內容易懷孕
	bra = last_date + timedelta(days=17)

	if choice == 'all' :
		content = ''
		content += user_name + ' 你好~\n'
		content += '你上次紀錄的日期是' + last_date_str + '\n\n'
		content += '預計下一次差不多會是' + period.strftime("%m/%d") + '來\n\n'
		content += preg.strftime("%m/%d") + ' 開始的一週很容易懷孕 (╯°Д°)╯ ┻━┻\n\n'
		content += diet.strftime("%m/%d") + ' 開始的一週內少吃多動會瘦很快!!\n\n'
		content += bra.strftime("%m/%d") + ' 開始的一週多按摩奶奶會長很大唷\n\n'
		return content
	elif choice =='上一次' :
		content = ''
		content += user_name + ' 你好~\n'
		content += '你上次紀錄的日期是' + last_date_str + ''
		return content
	elif choice =='下一次' :
		content = ''
		content += user_name + ' 你好~\n'
		content += '預計下一次差不多會是' + period.strftime("%m/%d") + '來'
		return content			
	elif choice =='瘦身' :
		content = ''
		content += user_name + ' 你好~\n'
		content += diet.strftime("%m/%d") + ' 開始的一週內少吃多動會瘦很快!!'
		return content
	elif choice =='豐胸' :
		content = ''
		content += user_name + ' 你好~\n'
		content += bra.strftime("%m/%d") + ' 開始的一週多按摩奶奶會長很大唷'
		return content
	elif choice =='危險' :
		content = ''
		content += user_name + ' 你好~\n'
		content += preg.strftime("%m/%d") + ' 開始的一週很容易懷孕 (╯°Д°)╯ ┻━┻'
		return content
	elif choice =='經期相關' :
		content = ''
		content += user_name + ' 你好~\n'
		content += '你上次紀錄的日期是' + last_date_str + '\n\n'
		content += '預計下一次差不多會是' + period.strftime("%m/%d") + '來\n\n'		
		content += '要注意!!\n' + preg.strftime("%m/%d") + ' 開始的一週很容易懷孕 (╯°Д°)╯ ┻━┻'
		return content