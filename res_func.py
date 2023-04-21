import requests
import os
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv("KEY")

def get_help():
	return """Dùng tiền tố '$' để chat công khai,  '?' để chat cá nhân

            `$help` : Như bạn có thể thấy.

            `$roll` : Một con số ngẫu nhiên từ 1 -> 6.

            `$feedback` <Nội dung>: Gửi phản hồi, bình luận, ... của bạn về bot chat.

            `$quote` <category | optional>: Trích dẫn ngẫu nhiên. 
            Có thể chọn trích dẫn thuộc các nhãn sau:
            age, alone, amazing, anger, architecture, art, attitude, beauty, 
            best, birthday, business, car, change, communications, computers, 
            cool, courage, dad, dating, death, design, dreams, education, 
            environmental, equality, experience, failure, faith, family, 
            famous, fear, fitness, food, forgiveness, freedom, friendship, 
            funny, future, god, good, government, graduation, great, happiness, 
            health, history, home, hope, humor, imagination, inspirational, 
            intelligence, jealousy, knowledge, leadership, learning, legal, life, 
            love, marriage, medical, men, mom, money, morning, movies, success.

            `$fact` : Một sự thật ngẫu nhiên.

            `$facts` <n> : n sự thật ngẫu nhiên (1<n<30).

            `$air` <city | required>: Thông tin về chất lượng không khí tại thành phố (tên tiếng anh).
            (Một vài từ khóa thành phố: Hanoi, Ho Chi Minh City, Danang, ...)

            `$weather` <city>: Thông tin về thời tiết tại thành phố (tên tiếng anh)
            (Một vài từ khóa thành phố: Hanoi, Ho Chi Minh City, Danang, ...)
            
        Trong tương lai:
        	`$decide` : Giống quyển sách "Vị thần của những quyết định"
            """

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

def convert_time(unix_timestamp):
    return datetime.fromtimestamp(unix_timestamp, timezone.utc).strftime('%d-%m-%Y %H:%M:%S')


## function that gets the weather
# Got some bugs
def get_weather(city = "Hanoi"):

    wind_direction = ["Gió Bắc","Gió Đông Bắc lệch Bắc","Gió Đông Bắc","Gió Đông Bắc lệch Đông",
    "Đông", "Gió Đông Nam lệch Đông", "Gió Đông Nam", "Gió Đông Nam lệch Nam",
    "Gió Nam", "Gió Tây Nam lệch Nam", "Gió Tây Nam", "Gió Tây Nam lệch Tây",
    "Gió Tây", "Gió Tây Bắc lệch Tây", "Gió Bắc Tây", "Gió Bắc Tây lệch Bắc"]

    WEATHER_URL = f'https://api.api-ninjas.com/v1/weather?city={city}'

    try:
        response = requests.get(WEATHER_URL, headers={'X-Api-Key': KEY})
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

def get_air_quality(city = "Hanoi"):

    city = city.lower()
    API_URL = f'https://api.api-ninjas.com/v1/airquality?city={city}'

    try:
        response = requests.get(API_URL, headers={'X-Api-Key': KEY})

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