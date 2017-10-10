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
                                                             
                                                       
     if message.text == "test":
         answer = "вроде работает"
         log(message,answer)
         bot.send_message(message.chat.id, answer)
                                                               
     elif message.text == "привет" or message.text == "Привет":
         answer = "привет, "
         log(message, answer)
         bot.send_message(message.chat.id, answer + message.from_user.first_name)
    else:
        bot.send_message(message.chat.id, answer)
         log(message,answer)
                                                               
   # для напомналки о ДР                                                            
"""from datetime import datetime
deadline = datetime.strptime("22/05/2017", "%d/%m/%Y")
print(deadline)     # 2017-05-22 00:00:00 """

 bot.polling(none_stop=True, interval=0)
