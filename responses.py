import random
from res_func import get_random_quote, get_weather, get_fact, save_feedback


def handle_response(username, message) -> str:

    if username == "Sadohpv#1252" or username == "Sadohpv#8885":
        return f"||You are gay! {username[:-5]}||"

    p_message = message.lower()

    if p_message == 'hello':
        return f'Hi! {username}'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == 'help':
        return  """Use PREFIX '$'' for chat in public, PREFIX '?' for private

            `$help` : As you can see.

            `$roll` : Random 1 to 6.

            `$feedback` <content>: send you feedback, repost, comment, etc...

            `$quote` <category | optional>: Ramdom quote about <category>. 
            Category used to limit results. Possible values are:
            age, alone, amazing, anger, architecture, art, attitude, beauty, 
            best, birthday, business, car, change, communications, computers, 
            cool, courage, dad, dating, death, design, dreams, education, 
            environmental, equality, experience, failure, faith, family, 
            famous, fear, fitness, food, forgiveness, freedom, friendship, 
            funny, future, god, good, government, graduation, great, happiness, 
            health, history, home, hope, humor, imagination, inspirational, 
            intelligence, jealousy, knowledge, leadership, learning, legal, life, 
            love, marriage, medical, men, mom, money, morning, movies, success.

            `$fact` : Random a fact.

            `$facts` <n> : Random n facts (1<n<30).

        In future:
            `$weather` <city>: Information about weather in city
            `$air`: Information about air quality
            """

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
        return get_fact(p_message[6])

    return 'Yeah, I don\'t know. Try typing "$help".'
