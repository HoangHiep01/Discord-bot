import requests
import os
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv("KEY")

def save_feedback(username, p_message):
	filename = username.replace("#", "_")
	path = f"feedback\\{filename}.txt"
	with open(file = path, mode = "a", encoding = 'utf-8') as f:
		f.write(p_message[9:] + '\n')
	return "Thank bro"

## function that gets the random quote
def get_random_quote(category = None):

	QUOTE_URL = 'https://api.api-ninjas.com/v1/quotes'

	if category is not None:
		category = category.lower()
		QUOTE_URL = f'https://api.api-ninjas.com/v1/quotes?category={category}'

	try:
		response = requests.get(QUOTE_URL, headers={'X-Api-Key': KEY})
		if response.status_code == requests.codes.ok:
			data = response.json()
			quote = data[0]['quote']
			author = data[0]['author']
			return f'"{quote}" - {author}'
		else:
			return f"Error - {response.status_code} - {response.text} - Your code and mine said. \n Of couse, if you write code."
	except:
		return "Something went wrong! Try Again! - Your code and mine said"

## function that gets the weather
# Got some bugs
def get_weather(city = "Hanoi"):

    WEATHER_URL = f'https://apihttps://api.api-ninjas.com/v1/weather?city={city}'

    try:
        response = requests.get(WEATHER_URL, headers={'X-Api-Key': KEY})
        if response.status_code == requests.codes.ok:
            data = response.json()
            return f"""Tốc độ gió: {data[0]["wind_speed"]}
            Nhiệt độ gió: {data[0]["wind_speed"]}
            Nhiệt độ: {data[0]["wind_speed"]}
            Độ ẩm: {data[0]["wind_speed"]}
            """
        else:
            return f"Error - {response.status_code} - {response.text}.\n Yeah! It's touch grass's time."
    except:
        return "Stand up and look out the window. You will see what ever you want, but my boss see some bugs"

## function that gets the fact
def get_fact(limit = 1):
	FACT_URL = f"https://api.api-ninjas.com/v1/facts?limit={limit}"

	try:
		response = requests.get(FACT_URL, headers={'X-Api-Key': KEY})
		if response.status_code == requests.codes.ok:
			datas = response.json()
			res = 'Did you know:\n'
			for data in datas:
				fact = data['fact']
				res += f'- {fact} \n'
			return res
		else:
			# return f"Error - {response.status_code} - {response.text}"
			return f"""Bạn có biết: Khi lập trình mà gặp lỗi là một điều bình thường.
		Đây thông báo khi code của tôi gặp lỗi: {response.status_code} - {response.text}.
		Xin cảm ơn!"""
	except:
		return """Bạn có biết: Khi lập trình mà gặp lỗi là một điều bình thường.
		Đây thông báo khi code của tôi gặp lỗi. 
		Xin cảm ơn!"""