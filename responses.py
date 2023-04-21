import random
from res_func import *


def handle_response(username, message) -> str:

    if username == "Sadohpv#1252" or username == "Sadohpv#8885":
        return f"||You are gay! {username[:-5]}||"

    p_message = message.lower()

    if p_message == 'hello':
        return f'Hi! {username}'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == 'help':
        return  get_help()

    if p_message.startswith('feedback '):
        return save_feedback(username, p_message)

    if p_message == 'quote':
        return get_random_quote()

    if p_message.startswith('quote'):
        return get_random_quote(p_message[6:])

    if p_message.startswith('weather'):
        return get_weather(p_message[8:])

    if p_message == "fact":
        return get_fact()

    if p_message.startswith("facts"):
        return get_fact(p_message[6:])

    if p_message.startswith("air"):
        return get_air_quality(p_message[4:])

    return 'Yeah, I don\'t know. Try typing "$help".'
