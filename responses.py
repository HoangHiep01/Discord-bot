import random
from res_func import *
from response.NinjasAPI import *

API = NinjasAPI()

def handle_response(username, message) -> str:

    if username == "Sadohpv#1252" or username == "Sadohpv#8885":
        return f"||You are gay! {username[:-5]}||"

    p_message = message.lower()

    if p_message == 'hello':
        return f'Hi! {username}'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message.startswith('feedback '):
        return save_feedback(username, p_message)

    if p_message == 'quote':
        return API.get_random_quote()

    if p_message.startswith('quote'):
        return API.get_random_quote(p_message[6:])

    if p_message.startswith('weather'):
        return API.get_weather(p_message[8:])

    if p_message == "fact":
        return API.get_fact()

    if p_message.startswith("facts"):
        limit = p_message.replace("facts ", "")
        if limit.isdigit():
            return API.get_fact(int(limit))
        return "Ơ kìa bro! Nhập số đi, cả khoảng cách nữa.\n Xử lý mấy cái ngoại lệ mệt lắm!"

    if p_message.startswith("air"):
        return API.get_air_quality(p_message[4:])

    if p_message == 'help':
        return  get_help()

    return 'Yeah, I don\'t know. Try typing "$help".'
