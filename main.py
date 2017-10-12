# telegram bot for Barrel team

"""

 The first edition
 
 """

import telebot
import const
import list
 bot = telebot.TeleBot(const.token)

bot.send_message(const.my_id, "test")

upd = bot.get_updates()

print(upd)

 last_upd = upd[-1]

 message_from_user = last_upd.message

 print(message_from_user)

print(bot.get_me())

 def log(message, answer):
   print("\n --------------------")
    from datetime import datetime
   print(datetime.now())
  print("Сообщение от {0} {1} (id = {2}) \n Текст: {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                               print(answer)


 @bot.message_handler(commands = ['help'])
 def handle_text(message):
         bot.send_message(message.chat.id, """вроде все работает""")

 @bot.message_handler(content_types = ['text'])
 def handle_text(message):

     answer = "неизвестная команда"
                                                               
   #проверить!  
             # message.lower()  превраить слово в нижний регистр, чтобы избегать многочисленных проверок                                                        
                                                             
                                                       
     if message.text == list.lst[0]: # "помощь"
         answer = "тут будет заполнена инфа по командам бота"
         log(message,answer)
         bot.send_message(message.chat.id, answer)
                                                               
     elif message.text == list.lst[1]: #"привет"
         answer = "привет, "
         log(message, answer)
         bot.send_message(message.chat.id, answer + message.from_user.first_name)
                                                               
      elif message.text == list.lst[2]: # "хэй, баррель"
         answer = "Хэй, " 
         log(message, answer)
         bot.send_message(message.chat.id, answer + message.from_user.first_name+ "!")       
                                                               
      elif message.text == list.lst[3]: # "расписание"
         answer = "тут будет инфа по расписанию тренировок "
         log(message, answer)
         bot.send_message(message.chat.id, answer)                                                       
      
       elif message.text == list.lst[4]: # "кричалка" 
         answer = "тут будут слова кричалки"
         log(message, answer)
         bot.send_message(message.chat.id, answer)
                                                               
       elif message.text == list.lst[5]: #  "музыка"
         answer = "тут будет музыка для выступлений"
         log(message, answer)
         bot.send_message(message.chat.id, answer)                                                         
       
        elif message.text == list.lst[6]: # "новости"
         answer = "тут будет полезная инфа по разным предстоящим событиям"
         log(message, answer)
         bot.send_message(message.chat.id, answer)
       
         elif message.text == list.lst[7]: # "батуты"
         answer = "тут будет инфа про батуты"
         log(message, answer)
         bot.send_message(message.chat.id, answer)     
                                                               
         elif message.text == list.lst[8]: # "правила"  
         answer = "тут будет инфа про черлидинг в целом"
         log(message, answer)
         bot.send_message(message.chat.id, answer)    
                                                               
#    else:
#        bot.send_message(message.chat.id, answer)
#         log(message,answer)
                                                               
                                                             
       
       
      
       
       
      
       
       
       
                                                               
   # для напомналки о ДР                                                            
"""from datetime import datetime
deadline = datetime.strptime("22/05/2017", "%d/%m/%Y")
print(deadline)     # 2017-05-22 00:00:00 """

 bot.polling(none_stop=True, interval=0)
                                                               
                                                               
                                                               
  ###
                                                               
                                                               #
# telegram bot for Barrel team

"""

The first edition

"""

import telebot
import const
import list

bot = telebot.TeleBot(const.token)

#bot.send_message(const.my_id, "test")

upd = bot.get_updates()

#print(upd)

last_upd = upd[-1]

message_from_user = last_upd.message

print(message_from_user)

print(bot.get_me())

def log(message, answer):
    print("\n --------------------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1} (id = {2}) \n Текст: {3}".format(message.from_user.first_name,
                                                                  message.from_user.last_name,
                                                                  str(message.from_user.id),
                                                                  message.text))
    print(answer)


@bot.message_handler(commands = ['help'])
def handle_text(message):
        bot.send_message(message.chat.id, """вроде все работает""")

@bot.message_handler(content_types = ['text'])
def handle_text(message):

    answer = "неизвестная команда"

    if message.text.lower() == list.lst[0]: # "помощь"
         answer = "тут будет заполнена инфа по командам бота"
         log(message,answer)
         bot.send_message(message.chat.id, answer)

    elif message.text.lower() == list.lst[1]: #"привет"
         answer = "привет, "
         log(message, answer)
         bot.send_message(message.chat.id, answer + message.from_user.first_name)

    elif message.text == list.lst[2]: # "хэй, баррель"
         answer = "Хэй, "
         log(message, answer)
         bot.send_message(message.chat.id, answer + message.from_user.first_name+ "!")

    elif message.text == list.lst[3]: # "расписание"
         answer = "тут будет инфа по расписанию тренировок "
         log(message, answer)
         bot.send_message(message.chat.id, answer)

    elif message.text == list.lst[4]: # "кричалка"
         answer = "тут будут слова кричалки"
         log(message, answer)
         bot.send_message(message.chat.id, answer)

    elif message.text == list.lst[5]: #  "музыка"
         answer = "тут будет музыка для выступлений"
         log(message, answer)
         bot.send_message(message.chat.id, answer)

    elif message.text == list.lst[6]: # "новости"
         answer = "тут будет полезная инфа по разным предстоящим событиям"
         log(message, answer)
         bot.send_message(message.chat.id, answer)

    elif message.text == list.lst[7]: # "батуты"
         answer = "тут будет инфа про батуты"
         log(message, answer)
         bot.send_message(message.chat.id, answer)

    elif message.text == list.lst[8]: # "правила"
         answer = "тут будет инфа про черлидинг в целом"
         log(message, answer)
         bot.send_message(message.chat.id, answer)


    else:
        bot.send_message(message.chat.id, answer)
        log(message,answer)


bot.polling(none_stop=True, interval=0)
                                                               
