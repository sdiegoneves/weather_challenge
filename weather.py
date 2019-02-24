import json, requests, datetime

class Weather:
	api_key = "1069338b53130cb70404de749808bdaa"
	url = "http://api.openweathermap.org/data/2.5/weather?q={},{}&APPID={}"
	forcast_url = "http://api.openweathermap.org/data/2.5/forecast?q={},{}&appid={}"

	def validate_city(self, city_name, country_code):
		call_url = self.url.format(city_name, country_code, self.api_key)
		response = requests.get(call_url)
		if response.status_code != 200:
			return False
		return True

	def getForcast(self, city_name, country_code, qtd_days = 6):
		
		call_url = self.forcast_url.format(city_name, country_code, self.api_key)
		response = requests.get(call_url)
		forcast = json.loads(response.content)
			
		return forcast['list']