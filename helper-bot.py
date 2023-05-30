import os
import time
import random
import telebot
import openai
from telebot import types


users=[] #users's ids for tag them, bot takes automatically
specials=[] #admins's ids which one need to write with !

tagScripts=[" Bu gün sənə heç nə deməyəcəyəm, çünki sözlərim yetersizdir.",
" Gözlərimlə sənə dünyaları söyləyirəm, amma səssizlikdən başqa heç bir şey eşitmirəm.",
" Sənə olan sevgim dənizlərin kənarına çatmayıb, sonsuzluğa çatır.",
" Sənin üçün mən hər şeyi gözəl edə bilərəm, çünki səninlə hər şey mükəmməldir.",
" Sənə olan sevgim hər hansı bir sözlə ifadə edilə bilməz, çünki sənin üçün olan hisslərim sözlərə sığmır.",
" Gördüyümüz gözlərlə görməyən, eşitdiyimiz qulaqlarla eşitməyən, hiss etdiyimiz qəlbdə hiss etməyən varlıqları da qəbul edin.",
" Mənim üçün sənin mənə təqdim etdiyin gözlərindən daha dəyərli heç bir şey yoxdur.",
" Səni görmək mənə hər şeydən çox xoş gəlir, çünki səni gördükdə gözlərimə gözəl bir dünya açılır.",
" Səni sevərkən hər şeyə gücüm çatır, çünki sevgimiz dənizin özü kimi sonsuzdur.",
" Səninlə ola biləcəyim hər anı qıymətləndirirəm, çünki səninlə olan anlarım həyatımın ən xoş vaxtlarıdır.",
" Mən bir qrupu timsahlarla gülməyə davam edirəm.",
" Bu gün bir böyrək balası ilə suşi yedim.",
" Sincablar çayda biskvit yeyirlər.",
" Qaraqoyunlar mənim bağçımda futbol oynayır.",
" Timsahlar insanlardan daha yaxşı səski oxuyurlar.",
" Tüp balıqları ayın birində partisi keçirdilər.",
" Qaraca ilan evimin yanında banan ağacı qurdu.",
" Papağanlar səs üzrə Amerika qış meşəsində yarışırlar.",
" İncir quşları çölə kruq bəsləmək üçün getdi.",
" Dovşanlar nəticədə üzüm və şokoladla süfrədə qalxırlar.",
" Mən bir dəniz iguanasının gülümsədiyini gördüm.",
" Tutaqlıqdan azad olan itlər dans edərək rayonun mərkəzindəki hava limanına doğru yürüyüblər.",
" Salam dostum!",
" Salam, şampion!",
" Salam, xeyirli yeməklər!",
" Hey, adi birisi!",
" Necədir, dostum?",
" Necə keçir, dostum?",
" Necə gedir işlər, qardaş yada baci?",
" Salam, dostum, hər şey yaxşıdı?",
" Salam, günlük!",
" Salam, qarışıqlıq!",
" Salam, dostum, qal maşınım!",
" Salam, gündəlik!",
" Salam, dostum, qal canımdan!",
" Necə gedir işlər, dostum?",
" Nə var nə yox, dostum?",
" Salam, xalqımızın nümayəndəsi!",
" ne var ne yox",
"Hər zaman özünü inkişaf etdirmək üçün çalışan bir insan.",
"Çox çalışğı, və işinə qarşı məsuliyyətli yanaşır.",
"Əməkdaşları ilə əlaqələri çox yaxşıdır və onları həmişə dəstəkləyir.",
"Məsuliyyətli və təşkilatlı bir şəkildə işlərini yerinə yetirir.",
"Həmişə inkişaf edən texnologiyalara diqqət yetirir və yeni şeylər öyrənmək üçün istəklidir.",
"İşinə qarşı məhəbbəti və təcrübəsi onu digərlərindən fərqləndirir.",
"Dərin analitik düşüncəsi və problemləri həll etmək üçün yaradıcılığı onun müvəffəqiyyətli olmasına səbəb olur.",
"Təcrübəli bir işçi olaraq, həmişə dəqiqliklə, təcrübə və qabiliyyət ilə işini həll edir.",
"Ən mühüm problemlərə yaxından baxmaq, həmişə təcrübəsini və biliklərini artırır.",
"Müsbət münasibəti ilə, özündən çox başqalarını da inkişaf etdirməyə nail olur.",
"İşinə təşviq etmək və başqa işçilərin iş qüvvəsindən ən yaxşı şəkildə istifadə etmək üçün yetərli məsuliyyət daşıyır.",
"Daima məqsədə nail olmaq üçün çətin işlərə təşkilatlanır və müvəffəqiyyətli olmaq üçün son qədər çalışır.",
"İşinin incəliklərinə diqqət yetirir və müştərilərini razı etmək üçün mükəmməl nəzarət edir.",
"Yeniliklərə açıq bir şəkildə baxır və daha yaxşı bir şirkət imkanı yaradmaq üçün fikirlər öyrənir və dəstəkləyir.",
"Həmişə özünü daha yüksək səviyyəyə aparacaq yeni yol tapmaq üçün fərqli məqamları araşdırır.",
"Mövqelərində vacib qərarlar vermək üçün həmişə düşünür və inkişaf etmək üçün özünü müqayisəyə salır.",
"Yaradıcılığı, problemləri həll etməyə və yenilikləri tətbiq etməyə həvəslidir.",
"Daima təcrübəsini artırmaq, yeni şeylər öyrənmək və inkişaf etmək üçün araşdırma aparır.",
"Məsuliyyətli və şəffaf bir şəkildə işini yerinə yetirir və müştəriləri ilə münasibət qurmaqda uğurlu olur.",
"Ən yaxşı yoldan, ən yaxşı nəticələr almaq üçün planlama, təşkilat və idarəetmə bacarığına malikdir.",
"Daima nəticəyə yönəlmiş olaraq, hər gün yeni məqsədlər qoyur və onlara çatmaq üçün çox çalışır."
]
BOT_TOKEN = 'YOUR_BOT_API_TOKEN'

bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
  tag=f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>'
  bot.send_message(message.chat.id, f'Salam xosh geldiniz {tag}!',parse_mode='HTML')

@bot.message_handler(commands=['menu'])
def menu(message):
  tag=f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>'
  markup = types.InlineKeyboardMarkup()
  button1 = types.InlineKeyboardButton("Bot rehberi", callback_data="bor_rehber")
  button2 = types.InlineKeyboardButton("Sahib", callback_data="Sahib")
  button3 = types.InlineKeyboardButton("Sahibe", callback_data="Sahibe")
  button5 = types.InlineKeyboardButton("Adminlist", callback_data="Adminlist")
  button6 = types.InlineKeyboardButton("Qrup", callback_data="Qrup")
  button7 = types.InlineKeyboardButton("Kanallar", callback_data="Kanallar")
  button8 = types.InlineKeyboardButton("Olmaz", callback_data="Olmaz")
  button9 = types.InlineKeyboardButton("Senin tagin", callback_data="tag")
  button10 = types.InlineKeyboardButton("Tagall", callback_data="tagall")
  markup.add(button2,button3)
  markup.add(button5,button1)
  markup.add(button6,button7,button8)
  markup.add(button9,button10)
  bot.send_message(message.chat.id, f'Salam xosh geldiniz {tag}!',parse_mode='HTML')
  bot.send_message(message.chat.id, "Hansi haqqinda gormek isterdiz?", reply_markup=markup)

openai.api_key = "YOUR_API_KEY"
def get_response(message):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{message}, write answer in Azerbaijani",
        max_tokens=1024,
        n=1,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

@bot.message_handler(commands=['starttag'])
def startTag(message):
  global stoptag
  if message.from_user.id not in users:
    users.append(message.from_user.id)

  chat_id = message.chat.id
  user_id = message.from_user.id
  chat_member = bot.get_chat_member(chat_id, user_id)

  if chat_member.status == 'administrator' or chat_member.status=="creator":
    stoptag=False
  else:
      bot.reply_to(message, 'dayan dostum admin deyilsen.')

  counter=0
  if (stoptag==False):
    if(len(users)<3):
      bot.reply_to(message, "bir gun qrupda herkesi tag edecem")
    else:
      for i in range(len(users)):
        tagWords = tagScripts[random.randint(0,len(tagScripts)-1)]
        index=random.randint(0, len(users)-1)
        member = bot.get_chat_member(chat_id, users[index])
        if member.user.is_bot: # skip over bots
            continue
        else:
          mention = f'<a href="tg://user?id={member.user.id}">{member.user.first_name+" "+tagWords}</a>'
          bot.send_message(chat_id, mention, parse_mode='HTML')
          counter+=1
          time.sleep(1)
          if(stoptag==True):
            break
    bot.send_message(chat_id,f"{counter} nefer tag olundu")
@bot.message_handler(commands=['stoptag'])
def stopTag(message):
  global stoptag
  chat_id = message.chat.id
  user_id = message.from_user.id
  chat_member = bot.get_chat_member(chat_id, user_id)

  if chat_member.status == 'administrator' or chat_member.status=="creator":
      stoptag=True
  else:
      bot.reply_to(message, 'dayan dostum admin deyilsen.')

@bot.message_handler(func=lambda msg: True)
def replys(message):
  if message.from_user.id not in users:
    users.append(message.from_user.id)
  chat_id = message.chat.id
  user_id = message.from_user.id
  chat_member = bot.get_chat_member(chat_id, user_id)

  if chat_member.status == 'administrator' and message.text[0]=="!" and user_id not in specials:
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
  message.text=message.text.capitalize()
  if(message.text=="Bot rehberi"):
    bot.reply_to(message, "@Ellnurr")
  elif(message.text=="Sahib"):
    bot.reply_to(message, "@nukredit1453")
  elif(message.text=="Sahibe"):
    bot.reply_to(message, "@Ahmdva22")
  elif(message.text=="Ass"):
    bot.reply_to(message, f"{message.from_user.first_name} Xeberin var bu normal soz deyil?")
  elif(message.text=="Adminlist"):
    try:
        chat_id = message.chat.id
        admins = bot.get_chat_administrators(chat_id)
        admin_list = "\n ".join([f"{f'@{admin.user.username} - {admin.user.first_name}' if admin.user.username else f'{admin.user.first_name}'} ({admin.status})" for admin in admins])
        bot.reply_to(message, admin_list)
    except Exception as e:
      bot.reply_to(message, "bu indiki adminlist olmaya biler indiki adminlisti gormek ucun qrupda bu sozu yazin. \n 🇦🇿 𝐎𝐋𝐃 𝐀𝐙𝐄 𝐌𝐀𝐅İ𝐀 🇹🇷 qrupundakı adminlər: \n- @Farruxxkh \n- @Ahmdva22 \n- @salamaybrat \n- 🌙Nezri🌹 \n- @nukredit1453 \n- 𝐅𝐢𝐚𝐚 𝐅𝐃ᥫ᭡ \n- @angelanila \n- @Glmlyvv \n- @Hshshshshshshshshshshhheh\n- @Azzardii\n- ᐯᗴᑕՏIᘔ𓅓🇷🇺\n- @maraglideyil\n- @ismayylovvv\n- @Ellnurr\n- @cekatuna\n- @Hsnv007\n- @faariddi\n- @esracikk\n- 𝓛𝓪𝓶𝓲𝔂𝓮 𝓛𝓾𝓷𝓪𓃠\n- @fariddnasirr\n- 🫧\n- @AytacAbd0va\n- @nurrcan22\n- @HzadeAyxan\n- 𝐍𝐢𝐠𝐠𝐚𝐫🦈\n- @Guerra1917\n- @Mikayilovhk")

  elif(message.text=="Qrup"):
    bot.reply_to(message, "https://t.me/OldAzeFamily")
  elif(message.text=="Kanallar"):
    bot.reply_to(message, "@OldAzeQayda \n @azeoldfban \n @oldazeblog")
  elif(message.text == "Olmaz"):
    bot.reply_to(message,"Soyus\nReklam\nAdam dasima")
  elif(message.text=="Tag"):
    user_id = message.from_user.id
    mention = f'<a href="tg://user?id={user_id}">{message.from_user.first_name}</a>'
    bot.reply_to(message, mention, parse_mode='HTML')
  else:
    text = message.text.upper()
    if(message.chat.id!=message.from_user.id):
      if("@OLDAZEHELPER_BOT" in text and "/STARTTAG" not in text and len(text)>len("@OLDAZEHELPER_BOT")):
        response = get_response(text.replace("@OLDAZEHELPER_BOT", ""))
        bot.reply_to(message, response)
    else:
      response = get_response(text)
      bot.reply_to(message, response)

@bot.callback_query_handler(func=lambda call: call.data == 'bor_rehber')
def bor_rehber(call):
  bot.send_message(call.message.chat.id, '@Ellnurr')
@bot.callback_query_handler(func=lambda call: call.data == 'Sahib')
def bor_rehber(call):
  bot.send_message(call.message.chat.id, '@nukredit1453')
@bot.callback_query_handler(func=lambda call: call.data == 'Sahibe')
def bor_rehber(call):
  bot.send_message(call.message.chat.id, '@Ahmdva22')
@bot.callback_query_handler(func=lambda call: call.data == 'Adminlist')
def bor_rehber(call):
  try:
        chat_id = call.message.chat.id
        admins = bot.get_chat_administrators(chat_id)
        admin_list = "\n ".join([f"{f'@{admin.user.username} - {admin.user.first_name}' if admin.user.username else f'{admin.user.first_name}'} ({admin.status})" for admin in admins])
        bot.send_message(call.message.chat.id, admin_list)
  except Exception as e:
      bot.send_message(call.message.chat.id, "bu indiki adminlist olmaya biler indiki adminlisti gormek ucun qrupda bu sozu yazin. \n 🇦🇿 𝐎𝐋𝐃 𝐀𝐙𝐄 𝐌𝐀𝐅İ𝐀 🇹🇷 qrupundakı adminlər: \n- @Farruxxkh \n- @Ahmdva22 \n- @salamaybrat \n- 🌙Nezri🌹 \n- @nukredit1453 \n- 𝐅𝐢𝐚𝐚 𝐅𝐃ᥫ᭡ \n- @angelanila \n- @Glmlyvv \n- @Hshshshshshshshshshshhheh\n- @Azzardii\n- ᐯᗴᑕՏIᘔ𓅓🇷🇺\n- @maraglideyil\n- @ismayylovvv\n- @Ellnurr\n- @cekatuna\n- @Hsnv007\n- @faariddi\n- @esracikk\n- 𝓛𝓪𝓶𝓲𝔂𝓮 𝓛𝓾𝓷𝓪𓃠\n- @fariddnasirr\n- 🫧\n- @AytacAbd0va\n- @nurrcan22\n- @HzadeAyxan\n- 𝐍𝐢𝐠𝐠𝐚𝐫🦈\n- @Guerra1917\n- @Mikayilovhk")

@bot.callback_query_handler(func=lambda call: call.data == 'Qrup')
def bor_rehber(call):
  bot.send_message(call.message.chat.id, 'https://t.me/OldAzeFamily')
@bot.callback_query_handler(func=lambda call: call.data == 'Kanallar')
def bor_rehber(call):
  bot.send_message(call.message.chat.id, '@OldAzeQayda \n @azeoldfban \n @oldazeblog')
@bot.callback_query_handler(func=lambda call: call.data == 'Olmaz')
def bor_rehber(call):
  bot.send_message(call.message.chat.id, 'Soyus\nReklam\nAdam dasima')
@bot.callback_query_handler(func=lambda call: call.data == 'tag')
def bor_rehber(call):
  user_id = call.from_user.id
  mention = f'<a href="tg://user?id={user_id}">{call.from_user.first_name} - @{call.from_user.username}</a>'
  bot.send_message(call.message.chat.id, mention, parse_mode='HTML')
@bot.callback_query_handler(func=lambda call: call.data == 'tagall')
def bor_rehber(call):
  chat_id=call.message.chat.id
  bot.send_message(call.message.chat.id, 'bir gun herkesi tag edecem')


bot.infinity_polling(none_stop=True)
