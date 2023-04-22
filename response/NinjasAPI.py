import requests
import os
from dotenv import load_dotenv


class NinjasAPI():

	def __init__(self):
		load_dotenv()
		self._KEY = os.getenv("KEY")
		self.BASE_URL = "https://api.api-ninjas.com/v1/"

	def get_random_quote(self, category=None):

		QUOTE_URL = self.BASE_URL + 'quotes'

		if category is not None:
			category = category.lower()
			QUOTE_URL = self.BASE_URL + f'quotes?category={category}'

		try:
			response = requests.get(QUOTE_URL, headers={'X-Api-Key': self._KEY})
			if response.status_code == requests.codes.ok:
				data = response.json()
				quote = data[0]['quote']
				author = data[0]['author']
				return f'"{quote}" - {author}'
			else:
				return f"Error - {response.status_code} - {response.text} - Your code and mine said. \n Of couse, if you write code."

		except:
			return "Something went wrong! Try Again! - Your code and mine said"

	def convert_time(self, unix_timestamp):
		return datetime.fromtimestamp(unix_timestamp, timezone.utc).strftime('%d-%m-%Y %H:%M:%S')

	def get_weather(self, city="Hanoi"):

		wind_direction = ["Gió Bắc", "Gió Đông Bắc lệch Bắc", "Gió Đông Bắc", "Gió Đông Bắc lệch Đông",
	    "Đông", "Gió Đông Nam lệch Đông", "Gió Đông Nam", "Gió Đông Nam lệch Nam",
	    "Gió Nam", "Gió Tây Nam lệch Nam", "Gió Tây Nam", "Gió Tây Nam lệch Tây",
	    "Gió Tây", "Gió Tây Bắc lệch Tây", "Gió Bắc Tây", "Gió Bắc Tây lệch Bắc"]

		WEATHER_URL = self.BASE_URL + f'weather?city={city}'

		try:
			response = requests.get(WEATHER_URL, headers={'X-Api-Key': self._KEY})
			if response.status_code == requests.codes.ok:
				data = response.json()
				return f"""Nhiệt độ: {data["temp"]}°C
Nhiệt độ cao nhất: {data["max_temp"]}°C
Nhiệt độ thấp nhất: {data["min_temp"]}°C
Cảm giác: {data["feels_like"]}°C
Độ ẩm: {data["humidity"]}%
Hướng gió: {data["wind_degrees"]}° - {wind_direction[round(int(data["wind_degrees"])/22.5)]}
Tốc độ gió: {data["wind_speed"]} m/s
Tỉ lệ mây che phủ: {data["cloud_pct"]}%
"""
# Mặt trời mọc: {convert_time(int(data["sunrise"]))}
# Mặt trời lặn: {convert_time(int(data["sunset"]))}
			else:
				return f"Error - {response.status_code} - {response.text}.\nYeah! It's touch grass's time."
		except Exception as e:
			print(e)
			return "Stand up and look out the window. You will see what ever you want, but my boss see some bugs"

	def get_fact(self, limit = 1):
		FACT_URL = self.BASE_URL + f"facts?limit={limit}"

		try:
			response = requests.get(FACT_URL, headers={'X-Api-Key': self._KEY})
			if response.status_code == requests.codes.ok:
				datas = response.json()
				res = 'Did you know:\n'
				for data in datas:
					fact = data['fact']
					res += f'- {fact}.\n'
				if limit > 30:
					res += "- Vượt quá giới hạn 'n' rồi bạn ơi.\n"
				return res
			else:
				# return f"Error - {response.status_code} - {response.text}"
				return f"""Bạn có biết: Khi lập trình mà gặp lỗi là một điều bình thường.
Đây thông báo khi code của tôi gặp lỗi: code {response.status_code} - text {response.text}.
Xin cảm ơn!"""
		except:
			return """Bạn có biết: Khi lập trình mà gặp lỗi là một điều bình thường.
Đây thông báo khi code của tôi gặp lỗi. 
Xin cảm ơn!"""

	def get_air_quality(self, city = "Hanoi"):

		city = city.lower()
		API_URL = self.BASE_URL + f'airquality?city={city}'

		try:
			response = requests.get(API_URL, headers={'X-Api-Key': self._KEY})

			if response.status_code == requests.codes.ok:
				data = response.json()
				return f"""CO: {data["CO"]["concentration"]}(μg/m3) - {data["CO"]["aqi"]}(aqi)
NO2: {data["NO2"]["concentration"]}(μg/m3) - {data["NO2"]["aqi"]}(aqi)
O3: {data["O3"]["concentration"]}(μg/m3) - {data["O3"]["aqi"]}(aqi)
SO2: {data["SO2"]["concentration"]}(μg/m3) - {data["SO2"]["aqi"]}(aqi)
PM2.5: {data["PM2.5"]["concentration"]}(μg/m3) - {data["PM2.5"]["aqi"]}(aqi)
PM10: {data["PM10"]["concentration"]}(μg/m3) - {data["PM10"]["aqi"]}(aqi)
Overall: {data["overall_aqi"]}"""
			else:
				code = response.status_code
				text = response.text
				return f"{code} - {text}"
		except Exception as e:
			return f"Unexpected: {e}"