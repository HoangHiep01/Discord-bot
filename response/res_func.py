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

def get_dir_size_old(path='.'):
	total = 0
	for p in os.listdir(path):
		full_path = os.path.join(path, p)
		if os.path.isfile(full_path):
			total += os.path.getsize(full_path)
		elif os.path.isdir(full_path):
			total += get_dir_size_old(full_path)
	return total

def save_feedback(username, p_message):
	# 2*30 bytes = 1GB
	if get_dir_size_old(os.getcwd().replace("response", "feedback")) < 2**30:
		filename = username.replace("#", "_")
		path = f"feedback\\{filename}.txt"
		with open(file = path, mode = "a", encoding = 'utf-8') as f:
			f.write(p_message[9:] + '\n')
		return "Thank bro"
	return "Thank bro! Nhưng hệ thống quá tải"