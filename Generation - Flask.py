import os 
os.system('pip install flask')
os.system('pip install requests')
from flask import Flask
import requests
app = Flask(__name__)

@app.route('/generation-email/')
def gene():
	url = 'https://randommer.io/random-email-address'
	headers = {
		'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-length': '239',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '.AspNetCore.Antiforgery.9TtSrW0hzOs=CfDJ8DJ-g9FHSSxClzJ5QJouzeI7-q_vZxCnhkeFlGapcHZgJbZ-aP87NSgO15EqlMTNlpWsrTtDK8Qo_FkcelUen-XMHT8ZaUCFeGiAhGS8O7Ny-7XLvjZQza8gyEX141ln397mg-FwkxUmh8CBjHv4QKw',
        'origin': 'https://randommer.io',
        'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="98"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 11; M2103K19G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'}
	data = {
'number': '1',
'culture': 'en_US'
	}
	req = requests.post(url, headers=headers, data=data).text
	dat = req.replace('[','').replace(']','').split(',')
	for i in dat:
		email = i.replace('"','')
		return email
app.run()
