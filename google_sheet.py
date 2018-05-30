import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

#為了記錄到spreadsheet
def auth_gss_client(path, scopes):
	credentials = ServiceAccountCredentials.from_json_keyfile_name(path,scopes)
	return gspread.authorize(credentials)

def update_sheet(gss_client, key, item,the_day):
	theday = the_day
	userid = item
	check = find_user_period(gss_client, key, userid)
	if check == 0: #原本沒有紀錄
		wks = gss_client.open_by_key(key)
		sheet = wks.sheet1
		sheet.insert_row([userid,the_day], 2)
	else:
		wks = gss_client.open_by_key(key)
		sheet = wks.sheet1
		cell = sheet.find(userid)
		r = cell.row
		c = cell.col
		sheet.update_cell(r,c+1,theday)

def find_user_period(gss_client, key, userid):

	wks = gss_client.open_by_key(key)
	sheet = wks.sheet1
	try:
		cell = sheet.find(userid)
		r = cell.row
		c = cell.col
		period_day = sheet.cell(r,c+1).value
		return period_day
	except:
		return 0

def user_log(gss_client, key, userid,username,message):
	day = datetime.now().strftime("%Y-%m-%d")
	time = datetime.now().time().strftime("%H:%M:%S")
	wks = gss_client.open_by_key(key)
	sheet = wks.get_worksheet(1)
	sheet.insert_row([userid,username,day,time,message], 2)