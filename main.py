# telegram bot for Barrel team

"""

The first edition

"""

import telebot
import list
from _datetime import datetime
from telebot import types

bot = telebot.TeleBot(list.token)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = "неизвестная команда"

    bot.send_message(list.my_id, "Новое сообщение от: {0} {1} (id = {2}) (chat_id = {3})\n Текст: {4}".format(
        message.from_user.first_name,
        message.from_user.last_name,
        str(message.from_user.id),
        str(message.chat.id),
        message.text,
        ))

    if message.text.lower() == list.lst[0]:  # меню
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('скрыть кнопки')
        user_markup.row(list.lst[1])
        user_markup.row(list.lst[9])
        user_markup.row(list.lst[2])
        user_markup.row(list.lst[3], list.lst[4])
        user_markup.row(list.lst[5], list.lst[6])
        user_markup.row(list.lst[7])
        user_markup.row(list.lst[8])

        bot.send_message(message.from_user.id,
                         "Список команд: \nхэй, баррель! \nтренеры \nновости \nрасписание \nкричалка \nмузыка \nбатуты \nсостав команды \nчерлидинг как спорт",
                         reply_markup=user_markup)


    elif message.text.lower() == list.lst[1]:  # "хэй, баррель!"

        bot.send_photo(message.from_user.id, "AgADAgADV6kxGw28EUvtgj53bsTDLx_JDw4ABIHB1oFvir-2xNEBAAEC",
                       "Хэй, " + message.from_user.first_name + "!")


    elif message.text.lower() == list.lst[2]:  # "новости"
        answer = "❗❗❗ Необходимо принести Наташе:\n1. Копия паспорта \n2. Копия студенческого билета \n3. Справка из диспансера \n4.Квалификационная книжка с заполненными данными и с вклеенной фотографией \n 5. 1440 рублей за семинар со Стальцером"
        bot.send_message(message.from_user.id, answer)

    elif message.text.lower() == list.lst[3]:  # "расписание"
        answer = "Вторник с 18:30 до 21:30 в РГУ нефти и газа\nЧетверг с 19:15 до 21:30 в РГУ нефти и газа \nСуббота с 18:00 до 21:00 в РГУ нефти и газа"
        bot.send_message(message.from_user.id, answer)

    elif message.text.lower() == list.lst[4]:  # "кричалка"
        answer = "тут будут слова кричалки"
        bot.send_message(message.from_user.id, answer)

    elif message.text.lower() == list.lst[5]:  # "музыка"
        answer = "тут будет музыка для сорев"
        bot.send_message(message.from_user.id, answer)

    elif message.text.lower() == list.lst[6]:  # "батуты"
        answer = "Батуты! 🕸 \nДень: понедельник и пятница \nВремя: с 19:00 до 21:00. \nМесто: зал 'Do a flip' \nАдрес: Орджоникидзе 11,  метро Ленинский проспект. \nСтоимость: 500 руб.\n\nВопросы? Звони Азату 89250230239"
        bot.send_photo(message.from_user.id, list.pict[0], answer)

    elif message.text.lower() == list.lst[7]:  # "баррелята"
        answer = "люди Барреля с их ДР и телефонами"
        user_markup2 = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup2.row('меню')
        for name in list.names:
            user_markup2.row(name)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup2)

    elif message.text.lower() == list.lst[8]:  # "черлидинг как спорт"
        answer = "Черлидинг"
        user_markup3 = telebot.types.ReplyKeyboardMarkup(True, False)
        for name in list.lst2:
            user_markup3.row(name)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup3)

    elif message.text.lower() == list.lst2[2]:
        answer = ""
        for term in list.termins:
            answer += term +"\n\n"
        bot.send_message(message.from_user.id, answer)

    elif message.text.lower() == list.lst2[3]:
        answer = ""
        for term in list.nomins:
            answer += term +"\n\n"
        bot.send_message(message.from_user.id, answer)

    elif message.text.lower() == list.lst2[1]:
        answer = ""
        for hist in list.history:
            answer += hist +"\n"
        bot.send_message(message.from_user.id, answer)
        answer = ""
        for hist in list.history2:
            answer += hist +"\n"
        bot.send_message(message.from_user.id, answer)

    elif message.text.lower() == list.lst[9]:  # "тренеры"
        bot.send_photo(message.from_user.id, list.photo[40],
                       "{0}  {1}".format(list.names[40],list.tel[40]))
        bot.send_photo(message.from_user.id, list.photo[33],
                       "{0}  {1}".format(list.names[33],list.tel[33]))

    elif message.text.lower() == "скрыть кнопки":
        hide_markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, "как пожелаете", reply_markup=hide_markup)

    for nam in list.names:
        i = 0
        capt = ""
        if nam == message.text:
            i = list.names.index(nam)
            capt = "{0} \nТелефон: \n{1} \nДень Рождения: \n{2}" .format(list.names[i],
                                                                     list.tel[i],
                                                                     list.bdays[i])
            bot.send_photo(message.from_user.id, list.photo[i], capt)





@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    bot.send_message(list.my_id, "Новое сообщение от: {0} {1} (id = {2}) (chat_id = {3}) \nphoto_id: {4}\n"
                                  "описание: {5}".format(message.from_user.first_name,
                                                         message.from_user.last_name,
                                                         str(message.from_user.id),
                                                         str(message.chat.id),
                                                         message.photo[len(message.photo) - 1].file_id,
                                                         message.caption
                                                         ))
    bot.send_photo(list.my_id, message.photo[len(message.photo) - 1].file_id)

@bot.message_handler(content_types=['document'])
def handle_docs_photo(message):
    bot.send_message(list.my_id, "Новое сообщение от: {0} {1} (id = {2}) (chat_id = {3}) \nfile_id: {4}\n"
                                  "описание: {5}".format(message.from_user.first_name,
                                                         message.from_user.last_name,
                                                         str(message.from_user.id),
                                                         str(message.chat.id),
                                                         message.document.file_id,
                                                         message.caption
                                                         ))
    bot.send_document(list.my_id, message.document.file_id)


# тест работы switch кнопки
#
# keyboard = telebot.types.InlineKeyboardMarkup()
# switch_button = telebot.types.InlineKeyboardButton(text="Вся информация тут",callback_data=list.lst[6])#, switch_inline_query=list.lst[6])
# keyboard.add(switch_button)
# bot.send_message(list.my_id, list.batut, reply_markup=keyboard)
#
# @bot.callback_query_handler(func=lambda c: True)
# def inline(c):
#     if c.data == list.lst[6]:
#         answer = "Батуты! 🕸 \nДень: понедельник и пятница \nВремя: с 19:00 до 21:00. \nМесто: зал 'Do a flip' \nАдрес: Орджоникидзе 11,  метро Ленинский проспект. \nСтоимость: 500 руб.\n\nВопросы? Звони Азату 89250230239"
#         bot.send_photo(c.message.chat.id, list.pict[0], answer)
#
#

# тест url кнопки
#
#keyboard = types.InlineKeyboardMarkup()
#url_button = types.InlineKeyboardButton(text="Проголосовать", url="https://vk.com/cheergubkin?w=wall-51130462_738%2Fall")
#keyboard.add(url_button)
##bot.send_message(list.my_id, "Кто точно будет на семирнаре со Стальцером?", reply_markup=keyboard)
#
#bot.send_message(249424164, "прости, на радостях ему рассказал.. пошел вторую забивку делать")


#col =27
#bot.send_photo(list.my_id,format(list.photo[col]),"Сегодня празднует свой День Рождения {0}️{1}".format(list.names[col],list.bdtext))

#bot.send_message(230258701, "базаришь")
#bot.send_message(-179404215,"_")

bot.polling(none_stop=True, interval=0)
