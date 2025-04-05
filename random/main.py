import telebot
from random import randint
random=telebot.TeleBot("")

@random.message_handler(commands=['r'])
def message(message):
	try:
		text=message.text.split();text.pop(0)
		if int(text[0])<int(text[1]): random.reply_to(message, f"{randint(int(text[0]), int(text[1]))}")
		else: random.reply_to(message, f"{randint(int(text[1]), int(text[0]))}")
	except Exception as e: random.reply_to(message,e)

random.infinity_polling(none_stop=True, interval=0)