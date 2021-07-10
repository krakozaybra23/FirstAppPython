from pyowm import OWM
import telebot

owm = OWM('34724dcc9ff51f832326bb8693362ac5',)
bot = telebot.TeleBot('1827515180:AAH6e18PZxm24vBycVPYtSxrGds1Ywhpi7c', parse_mode=None)

@bot.message_handler(content_types=['text'])
def send_welcome(message):
    try:
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(message.text)
        w = observation.weather
        temp = w.temperature('celsius')['temp']
        answer = 'В городе' + ' ' + str(message.text) + ' ' + 'температура' + ' ' + str(temp)



        bot.send_message(message.chat.id, answer)
    except Exception:
        answer2 = 'Допущена ошибка при вводе названия города:' + ' ' + str(message.text)
        bot.send_message(message.chat.id, answer2)
        return answer2




bot.polling(none_stop = True)
