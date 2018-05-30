import gspread
from oauth2client.service_account import ServiceAccountCredentials

#為了記錄到spreadsheet
def auth_gss_client(path, scopes):
	credentials = ServiceAccountCredentials.from_json_keyfile_name(path,scopes)
	return gspread.authorize(credentials)
def update_sheet(gss_client, key, item,the_day):
	wks = gss_client.open_by_key(key)
	sheet = wks.sheet1
	sheet.insert_row([item,the_day], 2)
def find_user_period(gss_client, key, userid):
	print("窩要近來查了")
	print(userid)
	wks = gss_client.open_by_key(key)
	sheet = wks.sheet1
	try:
		print("我查到了")
		cell = sheet.find(userid)
		r = cell.row
		c = cell.col
		period_day = sheet.cell(r,c+1).value
		return period_day
	except:
		print("我查沒有")
		return 0