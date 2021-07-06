import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telebot import types
import config


token = config.token

bot = telebot.TeleBot(token=token)



@bot.message_handler(commands=['start'])
def start_button(message):
    markup = InlineKeyboardMarkup(row_width=1)
    btn2 = InlineKeyboardButton(text="🇸🇱Uz🇸🇱", callback_data="uz")
    markup.add(btn2)
    bot.send_message(message.chat.id, f"Xush kelibsiz, <b>{message.from_user.first_name} "
                                      f"{message.from_user.last_name}</b> Sizga yordam berishdan xursandmiz ! ",
                     parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    uzbtn1 = KeyboardButton(text="Normativ-huquqiy hujjatlar")
    uzbtn5 = KeyboardButton(text="Adabiyotlar")
    uzbtn7 = KeyboardButton(text="Nazorat savollari")
    uzbtn14 = KeyboardButton(text="Tarqatma materiallar")
    uzbtn18 = KeyboardButton(text="Anatatsiya")
    uzbtn21 = KeyboardButton(text="O'quv mashg'ulotlari")
    uzbtn22 = KeyboardButton(text="Baxolash mezoni")
    uzbtn24 = KeyboardButton(text="Mualliflar")
    uzbtn25 = KeyboardButton(text="🔙back menyuga")
    uzmarkup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    uzmarkup.add(uzbtn1, uzbtn5, uzbtn7,uzbtn14, uzbtn18,uzbtn21,uzbtn22, uzbtn24, uzbtn25)

    if call.data == "uz":
        bot.delete_message(call.from_user.id, message_id=call.message.id)
        bot.send_message(text="Xush kelibsiz", chat_id=call.from_user.id, reply_markup=uzmarkup)
        print(call)

@bot.message_handler(content_types=['text'])
def menu(message):
    get_mess = message.text
    chatid = message.chat.id

    if get_mess == "O'quv mashg'ulotlari":
        btn1 = KeyboardButton(text="Amaliy mashg'ulotlar")
        btn2 = KeyboardButton(text="Videolar")
        btn3 = KeyboardButton(text="Prezentatsiya")
        btn4 = KeyboardButton(text="Keys-stadi")
        btn5 = KeyboardButton(text="Masalalar to'plami")
        btn6 = KeyboardButton(text="Ma'ruzalar")
        btn16 = KeyboardButton(text="🔙back menyuga")
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn16)
        bot.send_message(chatid, text="Tanlang", reply_markup=markup)

    if get_mess == "Nazorat savollari":
        btn1 = KeyboardButton(text="Mustaqil ish mavzulari")
        btn2 = KeyboardButton(text="Test savollar")
        btn3 = KeyboardButton(text="Nazorat va Muhokama uchun savollar")
        btn4 = KeyboardButton(text="Nazorat ishi topshiriqlari")
        btn5 = KeyboardButton(text="Referat mavzulari")
        btn16 = KeyboardButton(text="🔙back menyuga")
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(btn1, btn2, btn3, btn4, btn5, btn16)
        bot.send_message(chatid, text="Tanlang", reply_markup=markup)

    if get_mess == "Adabiyotlar":
        btn1 = KeyboardButton(text="Fanga bog'liq bo'lgan xorijiy adabiyotlar")
        btn2 = KeyboardButton(text="Xorijiy adabiyotlar")
        btn3 = KeyboardButton(text="Fanga bog'liq o'zbek adabiyotlar")
        btn4 = KeyboardButton(text="O'zbek adabiyotlar ro'yxati")
        btn16 = KeyboardButton(text="🔙back menyuga")
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(btn1, btn2, btn3, btn4, btn16)
        bot.send_message(chatid, text="Tanlang", reply_markup=markup)

    if get_mess == "Normativ-huquqiy hujjatlar":
        btn1 = KeyboardButton(text="Fan dasturi")
        btn2 = KeyboardButton(text="Ishchi dasturi")
        btn3 = KeyboardButton(text="Kalendar rejasi")
        btn16 = KeyboardButton(text="🔙back menyuga")
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(btn1, btn2, btn3, btn16)
        bot.send_message(chatid, text="Tanlang", reply_markup=markup)

    if get_mess == "Tarqatma materiallar":
        btn1 = KeyboardButton(text="Tarqatma_materiallar")
        btn2 = KeyboardButton(text="Statistik formulalar")
        btn3 = KeyboardButton(text="Glossariy")
        btn16 = KeyboardButton(text="🔙back menyuga")
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(btn1, btn2, btn3, btn16)
        bot.send_message(chatid, text="Tanlang", reply_markup=markup)


    if get_mess == "Fan dasturi":
        with open("1.Fan dasturi/fan va dastur.pdf", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)


    if get_mess == "Ishchi dasturi":
        with open("2. Ishchi dastur/iw.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Kalendar rejasi":
        with open("3. Kalendar reja/calendar.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Ma'ruzalar":
        btn1 = KeyboardButton(text="Mavzu - 1")
        btn2 = KeyboardButton(text="Mavzu - 2")
        btn3 = KeyboardButton(text="Mavzu - 3")
        btn4 = KeyboardButton(text="Mavzu - 4")
        btn5 = KeyboardButton(text="Mavzu - 5")
        btn6 = KeyboardButton(text="Mavzu - 6")
        btn7 = KeyboardButton(text="Mavzu - 7")
        btn8 = KeyboardButton(text="Mavzu - 8")
        btn9 = KeyboardButton(text="Mavzu - 9")
        btn10 = KeyboardButton(text="Mavzu - 10")
        btn11 = KeyboardButton(text="Mavzu - 11")
        btn12 = KeyboardButton(text="Mavzu - 12")
        btn13 = KeyboardButton(text="Mavzu - 13")
        btn14 = KeyboardButton(text="Mavzu - 14")
        btn15 = KeyboardButton(text="Mavzu - 15")
        btn16 = KeyboardButton(text="🔙back menyuga")
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(btn1, btn2, btn3, btn4, btn5,  btn6,  btn7,  btn8,  btn9,  btn10,  btn11,  btn12,  btn13,  btn14,  btn15,  btn16)
        bot.send_message(chatid, text="Tanlang", reply_markup=markup)

    if get_mess == "Mavzu - 1":
        with open("4. Ma'ruzalar/1. Mavzu.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu - 2":
        with open("4. Ma'ruzalar/2. Mavzu.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu - 3":
        with open("4. Ma'ruzalar/3. Mavzu.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu - 4":
        with open("4. Ma'ruzalar/4. Mavzu.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu - 5":
        with open("4. Ma'ruzalar/5. Mavzu.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu - 6":
        with open("4. Ma'ruzalar/6. Mavzu.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu - 7":
        with open("4. Ma'ruzalar/7. Mavzu.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu - 8":
        with open("4. Ma'ruzalar/8. Mavzu.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu - 9":
        with open("4. Ma'ruzalar/9. Mavzu.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu - 10":
        with open("4. Ma'ruzalar/10. Mavzu.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu - 11":
        with open("4. Ma'ruzalar/11. Mavzu.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu - 12":
        with open("4. Ma'ruzalar/12. Mavzu.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu - 13":
        with open("4. Ma'ruzalar/13. Mavzu.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu - 14":
        with open("4. Ma'ruzalar/14. Mavzu.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu - 15":
        with open("4. Ma'ruzalar/15. Mavzu.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Fanga bog'liq bo'lgan xorijiy adabiyotlar":
        btn1 = KeyboardButton(text="1")
        btn2 = KeyboardButton(text="2")
        btn3 = KeyboardButton(text="3")
        btn4 = KeyboardButton(text="4")
        btn5 = KeyboardButton(text="🔙back menyuga")
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(chatid, text="Tanlang", reply_markup=markup)

    if get_mess == "1":
        with open("5. xorijiy adabiyotlar/1.pdf", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "2":
        with open("5. xorijiy adabiyotlar/2.pdf", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "3":
        with open("5. xorijiy adabiyotlar/3.pdf", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "4":
        with open("5. xorijiy adabiyotlar/4.pdf", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Glossariy":
        with open("6. Glossariy/glossariy..doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mustaqil ish mavzulari":
        with open("7. Mustaqil ish mavzulari/mustaqil ish mavzulari..doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Test savollar":
        with open("8. Test savollari/test savollari.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Nazorat va Muhokama uchun savollar":
        with open("9. Nazorat va muhokama uchun savollar/Q va SXS fanidan nazorat va muhokama savollari.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Statistik formulalar":
        with open("10. Statistik formulalar/Statistik formulalar.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Nazorat ishi topshiriqlari":
        with open("11. Nazorat ishi topshiriqlari/Q va SXS fanidan nazorat ishi topshiriqlari.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Referat mavzulari":
        with open("12. Referat mavzulari/Q va SXS fanidan referat mavzular.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Keys-stadi":
        with open("13. Keys - stadi/Q va SXS fanidan Keys - stadi.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Tarqatma_materiallar":
        with open("14. Tarqatma materiallar/Q va SXS fanidan tarqatma materiallar.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Xorijiy adabiyotlar":
        with open("15. Xorijiy adabiyotlar ruyxati/Q va SXS fanidan xorijiy adabiyotlar ruyxati.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Fanga bog'liq o'zbek adabiyotlar":
        btn1 = KeyboardButton(text="Milliy Hisoblar tizimi")
        btn2 = KeyboardButton(text="Moliya statistikasi")
        btn3 = KeyboardButton(text="Ergasheva.SH")
        btn4 = KeyboardButton(text="Uquv qo'lanma")
        btn5 = KeyboardButton(text="Statistika")
        btn6 = KeyboardButton(text="Statiskika bo'yicha praktikum")
        btn7 = KeyboardButton(text="Statistika darslik")
        btn8 = KeyboardButton(text="🔙back menyuga")
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(chatid, text="Tanlang", reply_markup=markup)


    if get_mess == "Milliy Hisoblar tizimi":
        with open("16. Fanga bog`liq o`zbek adabiyotlar/Milliy hisoblar izimi.pdf", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Moliya statistikasi":
        with open("16. Fanga bog`liq o`zbek adabiyotlar/Moliya statistikasi darslik.pdf", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Ergasheva.SH":
        with open("16. Fanga bog`liq o`zbek adabiyotlar/Q va SXS adabiyot ERGASHEVA SH.rtf", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Uquv qo'lanma":
        with open("16. Fanga bog`liq o`zbek adabiyotlar/Q va SXS fanidan uquv qullanma.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Statistika":
        with open("16. Fanga bog`liq o`zbek adabiyotlar/statistika.pdf", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Statiskika bo'yicha praktikum":
        with open("16. Fanga bog`liq o`zbek adabiyotlar/Statistika bo'yicha praktikum.pdf", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Statistika darslik":
        with open("16. Fanga bog`liq o`zbek adabiyotlar/Statistika  darslik.pdf", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Masalalar to'plami":
        with open("17. Maslalar to`plami/Q va SXS Statistikasi masalara to`plami.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Anatatsiya":
        with open("18. Anatatsiya/Q va SXS fanidan anatatsiy.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Prezentatsiya":
        btn1 = KeyboardButton(text="Mavzu -1")
        btn2 = KeyboardButton(text="Mavzu -2")
        btn3 = KeyboardButton(text="Mavzu -3")
        btn4 = KeyboardButton(text="Mavzu -4")
        btn5 = KeyboardButton(text="Mavzu -5")
        btn6 = KeyboardButton(text="Mavzu -6")
        btn7 = KeyboardButton(text="Mavzu -7")
        btn8 = KeyboardButton(text="Mavzu -8")
        btn9 = KeyboardButton(text="Mavzu -9")
        btn10 = KeyboardButton(text="Mavzu -10")
        btn11 = KeyboardButton(text="Mavzu -11")
        btn12 = KeyboardButton(text="Mavzu -12")
        btn13 = KeyboardButton(text="Mavzu -13")
        btn14 = KeyboardButton(text="Mavzu -14")
        btn15 = KeyboardButton(text="Mavzu -15")
        btn16 = KeyboardButton(text="🔙back menyuga")
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(btn1, btn2, btn3, btn4, btn5,  btn6,  btn7,  btn8,  btn9,  btn10,  btn11,  btn12,  btn13,  btn14,  btn15,  btn16)
        bot.send_message(chatid, text="Tanlang", reply_markup=markup)

    if get_mess == "Mavzu -1":
        with open("19. Prezentatsiya/1. Mavzu Qishloq xo’jalik statistikasining predmeti, uslubi va ko’rsatkichlari.ppt", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu -2":
        with open("19. Prezentatsiya/2. Mavzu Bozor iqtisodiyoti sharoitida qishloq xo’jaligi statistikasining roli.ppt", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu -3":
        with open("19. Prezentatsiya/3. Mavzu Qishloq xo’jalik yerlari va va ulardan foydalanish statistikasi.ppt", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu -4":
        with open("19. Prezentatsiya/4. Mavzu Dehqonchilik statistikasi.ppt", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu -5":
        with open("19. Prezentatsiya/5. Mavzu O’simlikchilik statistikasi.ppt", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu -6":
        with open("19. Prezentatsiya/6. Mavzu Chorvachilik statistikasi.ppt", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu -7":
        with open("19. Prezentatsiya/7. Mavzu Ishlab chiqarish harajatlari mahsulotlar tannarxi statistikasi.ppt", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu -8":
        with open("19. Prezentatsiya/8. Mavzu Iqtisodiyot tarmoqlarida suvdan foydalanish.ppt", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu -9":
        with open("19. Prezentatsiya/9. Mavzu Suv resurslaridan foydalanishning samaradorlik ko’rsatkichlari.ppt", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu -10":
        with open("19. Prezentatsiya/10. Mavzu Qishloq va suv xo’jaligi sohasiga kiritilgan investitsiyalar tahlili.ppt", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu -11":
        with open("19. Prezentatsiya/11. Mavzu Suv resurslarini etkazib berish uchun sarf-xarajatlar tahlili.ppt", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu -12":
        with open("19. Prezentatsiya/12. Mavzu Tabiiy resurslardan foydalanishning iqtisodiy-ekologik ko’rsatkichlari tahlili.ppt", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu -13":
        with open("19. Prezentatsiya/13. Mavzu Suv sifati va uni monitoringi.ppt", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu -14":
        with open("19. Prezentatsiya/14. Mavzu Suvdan barqaror foydalanish va uni asrash tadbirlari.ppt", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu -15":
        with open("19. Prezentatsiya/15. Mavzu Oqava suvlardan foydalanish.ppt", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Videolar":
        btn1 = KeyboardButton(text="Qishloq xo’jalik statistikasining...")
        btn2 = KeyboardButton(text="Bozor iqtisodiyoti sharoitida...")
        btn3 = KeyboardButton(text="Qishloq xo’jalik yerlari va ulardan..")
        btn4 = KeyboardButton(text="Dehqonchilik statistikasi")
        btn5 = KeyboardButton(text="O’simlikchilik statistikasi")
        btn6 = KeyboardButton(text="Chorvachilik statistikasi")
        btn7 = KeyboardButton(text="Ishlab chiqarish harajatlari...")
        btn8 = KeyboardButton(text="Iqtisodiyot tarmoqlarida suvdan...")
        btn9 = KeyboardButton(text="Suv resurslaridan foydalanishning..")
        btn10 = KeyboardButton(text="Qishloq va suv xo’jaligi...")
        btn11 = KeyboardButton(text="Suv resurslarini etkazib berish...")
        btn12 = KeyboardButton(text="Tabiiy resurslardan foydalanish...")
        btn13 = KeyboardButton(text="Suv sifati va uni monitoringi")
        btn14 = KeyboardButton(text="Suvdan barqaror foydalanish...")
        btn15 = KeyboardButton(text="Oqava suvlardan foydalanish")
        btn16 = KeyboardButton(text="🔙back menyuga")
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15,btn16)
        bot.send_message(chatid, text="Tanlang", reply_markup=markup)

    if get_mess == "Qishloq xo’jalik statistikasining...":
        btn3 = KeyboardButton(text="🔙back menyuga")
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        markup.add(btn3)
        bot.send_message(chatid, "Mover\nhttps://mover.uz/watch/3Q5NgBdy\nYoutube\nhttps://youtu.be/U5rEWWY_o8c",reply_markup=markup)

    if get_mess == "Bozor iqtisodiyoti sharoitida...":
        btn3 = KeyboardButton(text="🔙back menyuga")
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        markup.add(btn3)
        bot.send_message(chatid, "Mover\nhttps://mover.uz/watch/6RvhWuNV\nYoutube\nhttps://youtu.be/sTrsBNPihiY",reply_markup=markup)

    if get_mess == "Qishloq xo’jalik yerlari va ulardan..":
        btn3 = KeyboardButton(text="🔙back menyuga")
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        markup.add(btn3)
        bot.send_message(chatid, "Mover\nhttps://mover.uz/watch/fTR4Rx4A\nYoutube\nhttps://youtu.be/PCFHRFNp3Eo",
                         reply_markup=markup)

    if get_mess == "Dehqonchilik statistikasi":
        btn3 = KeyboardButton(text="🔙back menyuga")
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        markup.add(btn3)
        bot.send_message(chatid, "Mover\nhttps://mover.uz/watch/nzm7O0HJ\nYoutube\nhttps://youtu.be/9eJiTzy56jQ",
                         reply_markup=markup)

    if get_mess == "O’simlikchilik statistikasi":
        btn3 = KeyboardButton(text="🔙back menyuga")
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        markup.add(btn3)
        bot.send_message(chatid, "Mover\nhttps://mover.uz/watch/2irwaIkQ\nYoutube\nhttps://youtu.be/HiBBtPYiqH4",
                         reply_markup=markup)

    if get_mess == "Chorvachilik statistikasi":
        btn3 = KeyboardButton(text="🔙back menyuga")
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        markup.add(btn3)
        bot.send_message(chatid, "Mover\nhttps://mover.uz/watch/hQRWO4Km\nYoutube\nhttps://youtu.be/UZw3S4cJit4",
                         reply_markup=markup)

    if get_mess == "Ishlab chiqarish harajatlari...":
        btn3 = KeyboardButton(text="🔙back menyuga")
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        markup.add(btn3)
        bot.send_message(chatid, "Mover\nhttps://mover.uz/watch/9WR0V2Y\nYoutube\nhttps://youtu.be/m7kh7ZNae7w",
                         reply_markup=markup)

    if get_mess == "Iqtisodiyot tarmoqlarida suvdan...":
        btn3 = KeyboardButton(text="🔙back menyuga")
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        markup.add(btn3)
        bot.send_message(chatid, "Mover\nhttps://mover.uz/watch/qO2KVXdG\nYoutube\nhttps://youtu.be/Ma8dHa_hfbk",
                         reply_markup=markup)

    if get_mess == "Suv resurslaridan foydalanishning..":
        btn3 = KeyboardButton(text="🔙back menyuga")
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        markup.add(btn3)
        bot.send_message(chatid, "Mover\nhttps://mover.uz/watch/jsT8bIP6\nYoutube\nhttps://youtu.be/lcJ3-6GWUgk",
                         reply_markup=markup)

    if get_mess == "Qishloq va suv xo’jaligi...":
        btn3 = KeyboardButton(text="🔙back menyuga")
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        markup.add(btn3)
        bot.send_message(chatid, "Mover\nhttps://mover.uz/watch/vuGn4Uxi\nYoutube\nhttps://youtu.be/pjG4WSyV258",
                         reply_markup=markup)

    if get_mess == "Suv resurslarini etkazib berish...":
        btn3 = KeyboardButton(text="🔙back menyuga")
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        markup.add(btn3)
        bot.send_message(chatid, "Mover\nhttps://mover.uz/watch/Q7mcEB7I\nYoutube\nhttps://youtu.be/fgSmtEJ7Ifc",
                         reply_markup=markup)

    if get_mess == "Tabiiy resurslardan foydalanish...":
        btn3 = KeyboardButton(text="🔙back menyuga")
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        markup.add(btn3)
        bot.send_message(chatid, "Mover\nhttps://mover.uz/watch/h3IyrYzh\nYoutube\nhttps://youtu.be/PjvE0OW2yfU",
                         reply_markup=markup)

    if get_mess == "Suv sifati va uni monitoringi":
        btn3 = KeyboardButton(text="🔙back menyuga")
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        markup.add(btn3)
        bot.send_message(chatid, "Mover\nhttps://mover.uz/watch/kWvJjXb4\nYoutube\nhttps://youtu.be/XlyUGPQ1RN4",
                         reply_markup=markup)

    if get_mess == "Suvdan barqaror foydalanish...":
        btn3 = KeyboardButton(text="🔙back menyuga")
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        markup.add(btn3)
        bot.send_message(chatid, "Mover\nhttps://mover.uz/watch/eE55MrG6\nYoutube\nhttps://youtu.be/kF2yxzncYbU",
                         reply_markup=markup)

    if get_mess == "Oqava suvlardan foydalanish":
        btn3 = KeyboardButton(text="🔙back menyuga")
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        markup.add(btn3)
        bot.send_message(chatid, "Mover\nhttps://mover.uz/watch/M7IXuO1V\nYoutube\nhttps://youtu.be/i0FukvRljMg",
                         reply_markup=markup)

    if get_mess == "Amaliy mashg'ulotlar":
        btn1 = KeyboardButton(text="Mavzu-1")
        btn2 = KeyboardButton(text="Mavzu-2")
        btn3 = KeyboardButton(text="Mavzu-3")
        btn4 = KeyboardButton(text="Mavzu-4")
        btn5 = KeyboardButton(text="Mavzu-5")
        btn6 = KeyboardButton(text="Mavzu-6")
        btn7 = KeyboardButton(text="Mavzu-7")
        btn8 = KeyboardButton(text="Mavzu-8")
        btn9 = KeyboardButton(text="Mavzu-9")
        btn10 = KeyboardButton(text="Mavzu-10")
        btn11 = KeyboardButton(text="Mavzu-11")
        btn12 = KeyboardButton(text="Mavzu-12")
        btn13 = KeyboardButton(text="Mavzu-13")
        btn14 = KeyboardButton(text="Mavzu-14")
        btn15 = KeyboardButton(text="Mavzu-15")
        btn16 = KeyboardButton(text="🔙back menyuga")
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15,btn16)
        bot.send_message(chatid, text="Tanlang", reply_markup=markup)

    if get_mess == "Mavzu-1":
        with open("21. Amaliy mashg`ulotlari/1. Mavzu Qishloq xo’jalik statistikasining predmeti, uslubi va ko’rsatkichlari.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu-2":
        with open("21. Amaliy mashg`ulotlari/2. Mavzu Bozor iqtisodiyoti sharoitida qishloq xo’jaligi statistikasining roli.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu-3":
        with open("21. Amaliy mashg`ulotlari/3. Mavzu Qishloq xo’jalik yerlari va va ulardan foydalanish statistikasi.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu-4":
        with open("21. Amaliy mashg`ulotlari/4. Mavzu Dehqonchilik statistikasi.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu-5":
        with open("21. Amaliy mashg`ulotlari/5. Mavzu O’simlikchilik statistikasi.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu-6":
        with open("21. Amaliy mashg`ulotlari/6. Mavzu Chorvachilik statistikasi.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu-7":
        with open("21. Amaliy mashg`ulotlari/7. Mavzu Ishlab chiqarish harajatlari mahsulotlar tannarxi statistikasi.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu-8":
        with open("21. Amaliy mashg`ulotlari/8. Mavzu Iqtisodiyot tarmoqlarida suvdan foydalanish.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu-9":
        with open("21. Amaliy mashg`ulotlari/9. Mavzu Suv resurslaridan foydalanishning samaradorlik ko’rsatkichlari.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu-10":
        with open("21. Amaliy mashg`ulotlari/10. Mavzu Qishloq va suv xo’jaligi sohasiga kiritilgan investitsiyalar tahlili.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu-11":
        with open("21. Amaliy mashg`ulotlari/11. Mavzu Suv resurslarini etkazib berish uchun sarf-xarajatlar tahlili.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu-12":
        with open("21. Amaliy mashg`ulotlari/12. Mavzu Tabiiy resurslardan foydalanishning iqtisodiy-ekologik ko’rsatkichlari tahlili.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu-13":
        with open("21. Amaliy mashg`ulotlari/13. Mavzu Suv sifati va uni monitoringi.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu-14":
        with open("21. Amaliy mashg`ulotlari/14. Mavzu Suvdan barqaror foydalanish va uni asrash tadbirlari.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mavzu-15":
        with open("21. Amaliy mashg`ulotlari/15. Mavzu Oqava suvlardan foydalanish.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Baxolash mezoni":
        with open("22. Baholash mezoni/Q va SXS fanidan baholash mezoni.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "O'zbek adabiyotlar ro'yxati":
        with open("23. O`zbek adabiyotlar ro`yxati/Q va SXS fanidan adabiyotlar ruyxati.docx", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Mualliflar":
        btn1 = KeyboardButton(text="Raxmataliyev.M")
        btn2 = KeyboardButton(text="Axmedov.A")
        btn3 = KeyboardButton(text="Tashxodjaeva.G")
        btn4 = KeyboardButton(text="🔙back menyuga")
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(chatid, text="Tanlang", reply_markup=markup)

    if get_mess == "Raxmataliyev.M":
        with open("24. Mualliflar/Raxmataliyev Muzaffar Eshdavlatovich..doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Axmedov.A":
        with open("24. Mualliflar/Ахмедов_Азамат_Kamilovich..doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "Tashxodjaeva.G":
        with open("24. Mualliflar/Ташходжаева  Гулноза  Сайдамходжаевна.doc", "rb") as misc:
            f = misc.read()
        bot.send_document(chatid, f)

    if get_mess == "🔙back menyuga":
        uzbtn1 = KeyboardButton(text="Fan dasturi")
        uzbtn2 = KeyboardButton(text="Ishchi dasturi")
        uzbtn3 = KeyboardButton(text="Kalendar rejasi")
        uzbtn4 = KeyboardButton(text="Ma'ruzalar")
        uzbtn5 = KeyboardButton(text="Fanga bog'liq bo'lgan xorijiy adabiyotlar")
        uzbtn6 = KeyboardButton(text="Glossariy")
        uzbtn7 = KeyboardButton(text="Mustaqil ish mavzulari")
        uzbtn8 = KeyboardButton(text="Test savollar")
        uzbtn9 = KeyboardButton(text="Nazorat va Muhokama uchun savollar")
        uzbtn10 = KeyboardButton(text="Statistik formulalar")
        uzbtn11 = KeyboardButton(text="Nazorat ishi topshiriqlari")
        uzbtn12 = KeyboardButton(text="Referat mavzulari")
        uzbtn13 = KeyboardButton(text="Keys-stadi")
        uzbtn14 = KeyboardButton(text="Tarqatma materiallar")
        uzbtn15 = KeyboardButton(text="Xorijiy adabiyotlar")
        uzbtn16 = KeyboardButton(text="Fanga bog'liq o'zbek adabiyotlar")
        uzbtn17 = KeyboardButton(text="Masalalar to'plami")
        uzbtn18 = KeyboardButton(text="Anatatsiya")
        uzbtn19 = KeyboardButton(text="Prezentatsiya")
        uzbtn20 = KeyboardButton(text="Videolar")
        uzbtn21 = KeyboardButton(text="Amaliy mashg'ulotlar")
        uzbtn22 = KeyboardButton(text="Baxolash mezoni")
        uzbtn23 = KeyboardButton(text="O'zbek adabiyotlar ro'yxati")
        uzbtn24 = KeyboardButton(text="Mualliflar")
        uzbtn25 = KeyboardButton(text="🔙back menyuga")
        uzmarkup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        uzmarkup.add(uzbtn1, uzbtn2, uzbtn3, uzbtn4, uzbtn5, uzbtn6, uzbtn7, uzbtn8, uzbtn9, uzbtn10, uzbtn11, uzbtn12,
                     uzbtn13, uzbtn14, uzbtn15, uzbtn16, uzbtn17, uzbtn18, uzbtn19, uzbtn20, uzbtn21, uzbtn22, uzbtn23,
                     uzbtn24, uzbtn25)
        bot.send_message(chatid, "tanlang", reply_markup=uzmarkup)


bot.polling()



