import telebot
from telebot import types
orders=18
token='6277036977:AAH7FNm-02yIjN1eVp0fgTTMym-DQBfXFmM'
gl_admin = 1367133194
bot=telebot.TeleBot(token)
@bot.message_handler(commands=["start"])
def satrt(message):
      global menu
      menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("/close")
      btn2 = types.KeyboardButton("/open")
      menu.add(btn1, btn2)
      hi=bot.send_message(message.chat.id, "Меню".format(message.from_user),reply_markup=menu)
@bot.message_handler(commands=['open'])
def start_message(message):
    obrobot=open("admins.txt", "r")
    admins=obrobot.read()
    obrobot.close()
    if str(message.from_user.id) in admins:
      global markup 
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Да")
      btn2 = types.KeyboardButton("Нет")
      markup.add(btn1, btn2)
      hi=bot.send_message(message.chat.id, f"💭 Здравствуйте, {message.from_user.username}!\nХотите сделать набор на отзывы?".format(message.from_user),reply_markup=markup)
      
      obrobot.close()
      bot.register_next_step_handler(hi,yes)
    else:       
      bot.send_message(message.chat.id, "Доступ не обнаружен, для покупки, просим вас, написать - @Osiblion")
def yes(message):
      if message.text.lower() == "да":
          global markup2
          markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
          btn1 = types.KeyboardButton("Авито")
          btn2 = types.KeyboardButton("Яндекс Карты")
          btn3 = types.KeyboardButton("Google Карты")
          markup2.add(btn1,btn2,btn3)
          pl = bot.send_message(message.chat.id, "Выберите платформу:".format(message.from_user),reply_markup=markup2)
          bot.register_next_step_handler(pl,xz)
      elif message.text.lower() == "нет":
          bot.send_message(message.chat.id, "Пидора ответ)".format(message.from_user),reply_markup=types.ReplyKeyboardRemove())
          
def xz(message):
    global platform
    global plat
    plat=message.text.lower()
    platform=message.text.title()
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("60")
    btn2 = types.KeyboardButton("65")
    btn3 = types.KeyboardButton("70")
    btn4 = types.KeyboardButton("100")
    markup3.add(btn1,btn2,btn3,btn4)
    price=bot.send_message(message.chat.id, "Укажите оплату за отзыв:".format(message.from_user),reply_markup=markup3)
    bot.register_next_step_handler(price,mans)
def mans(message):
    global oplata
    oplata=message.text
    markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1")
    btn2 = types.KeyboardButton("3")
    btn3 = types.KeyboardButton("5")
    btn4 = types.KeyboardButton("10")
    markup4.add(btn1,btn2,btn3,btn4)
    kolov = bot.send_message(message.chat.id, "Укажите количество требуемых людей:".format(message.from_user),reply_markup=markup4)
    bot.register_next_step_handler(kolov,oplata_za_otziv)
def oplata_za_otziv(message):
    global chels
    chels=message.text
    comm=bot.send_message(message.chat.id, "Отлично, Ваш комментарий к набору:".format(message.from_user),reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(comm,com)
def com(message):
    global comment
    comment=message.text
    bot.send_message(message.chat.id,"Ожидайте, в канал поступит пост".format(message.from_user),reply_markup=menu)
    global orders
    orders+=1
    bot.send_message("@YakuzaAvito",f"🔰 Набор #{orders} открыт!\n🎁 {platform}\n👩‍🔧 Нужно людей: {chels}\n💵Оплата: {oplata}\n🏷 Описание: {comment}\n✉️ Писать - @{message.from_user.username}")
@bot.message_handler(commands=['myid'])
def myid(message):
    bot.send_message(message.chat.id, f"Ваш ID: {message.from_user.id}")
@bot.message_handler(commands=['addadmin'])
def addadmin(message):
    adminid = message.text.split(maxsplit=1)[1]
    if message.from_user.id == gl_admin or message.from_user.id == 5699395851:
        demo_file = open('admins.txt','a')
        demo_file.write(" "+adminid)
        demo_file.close()
        bot.send_message(message.chat.id,"Успешно!")
    else:
        bot.send_message(message.chat.id, "Произошла ошибка! Нет прав!")

@bot.message_handler(commands=['close'])
def get_link(message):
    a=bot.send_message(message.chat.id, "Введите номер набора:")
    bot.register_next_step_handler(a,get_number)
def get_number(message):
    global number
    number=message.text
    z=bot.send_message(message.chat.id, "Ссылку на пост:")
    bot.register_next_step_handler(z,close)
def close(message):
    link=message.text
    bot.edit_message_text(chat_id = "@YakuzaAvito", message_id = link[25:], text = f"❌ Набор #{number} был закрыт! Новые заявки не принимаются!")
@bot.message_handler(commands=['info'])
def info(message):
    if message.from_user.id==gl_admin or message.from_user.id==5699395851:
        inf=open("info.txt","r")
        bot.send_message(message.chat.id,*inf)
        inf.close()
    else:
        bot.send_message(message.chat.id,"Нет прав!")
@bot.message_handler(commands=["editinfo"])
def edit(message):
    d=bot.send_message(message.chat.id,"Текст инфо:")
    bot.register_next_step_handler(d,einfo)
def einfo(message):
    text=message.text
    file = open('info.txt','w')
    file.write(text)
    file.close()
@bot.message_handler(commands=["getadmins"])
def get(message):
    getadm=open("admins.txt","r")
    bot.send_message(message.chat.id,*getadm)
    getadm.close()
@bot.message_handler(commands=["changeadmins"])
def get1(message):
    if message.from_user.id==gl_admin or message.from_user.id==5699395851:
        getadms=open("admins.txt","r")
        k=bot.send_message(message.chat.id, "Введите замену списка:")
        getadms.close()
        bot.register_next_step_handler(k,get2)
    else:
        bot.send_message(message.chat.id, "У мужлана нету прав")
def get2(message):
    changtext=message.text
    changeadm=open("admins.txt","w")
    changeadm.write(changtext)
    changeadm.close()
    
bot.infinity_polling()
