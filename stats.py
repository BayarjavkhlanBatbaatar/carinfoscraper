import requests
import json

url = "http://api.marketcheck.com/v1/search"

querystring = {"api_key":"0I5Bg6okdYFVvKYsLdflgl0U1p2zOpfP","make":"ford","model":"f150","car_type":"used","start":"1","rows":"0","stats":"price","latitude":"34.05","longitude":"-118.24","radius":"100"}

headers = {'Host': 'marketcheck-prod.apigee.net'}

response = requests.request("GET", url, headers=headers, params=querystring)

response = response.text
response = json.loads(response)
for data in response:
	print(data)