from pyowm import OWM
import telebot

owm = OWM('34724dcc9ff51f832326bb8693362ac5',)
bot = telebot.TeleBot("1827515180:AAGU12vWKQsAh5jG4AYpWxPTNOX-P5IJF3s", parse_mode=None)

@bot.message_handler(content_types=['text'])
def send_welcome(message):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')['temp']
    answer = 'В городе' + ' ' + str(message.text) + ' ' + 'температура' + ' ' + str(temp)

    answer_two = 'проверьте правильность ввода города'

    bot.send_message(message.chat.id, answer)
else:
    bot.send_message(message.chat.id, answer_two)


bot.polling(none_stop = True)