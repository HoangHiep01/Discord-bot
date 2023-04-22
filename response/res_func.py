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