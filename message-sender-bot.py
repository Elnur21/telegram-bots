import telebot

# Replace YOUR_BOT_TOKEN with the bot token provided by BotFather
bot = telebot.TeleBot('YOUR_BOT_TOKEN')

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Salam! Mənə bir mesaj göndərin və mən sizdən bu mesajın anonim olmasını istəyib-istəmədiyinizi soruşacam.')


def ask_anonymous(message,message_text):
    chat_id = message.chat.id
    anonymous = message.text.lower() == 'bəli'
    # Get the username of the sender if the message is not anonymous
    username = message.from_user.first_name if not anonymous else 'Anonim'
    # Send the message to the channel with the appropriate prefix
    channel_id = '@YOUR_CHANNEL' 
    bot.send_message(chat_id=channel_id, text=f'🌟 Yeni bir cəsarətli istifadəçi mesajı👏👏 \n👤 {username} deyir ki: \n\n'+ message_text+f"\n\n💌 Etirafınızı @OLDAZEetiraf_bot botuna göndərin və bot onu paylaşcaq.😁")
    # Send a confirmation message to the user
    bot.send_message(chat_id=chat_id, text="Sizin mesajınız kanala göndərildi!")



@bot.message_handler(func=lambda message: True)
def store_message(message):
    # Get the message from the user's session data
    message_text = message.text
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Bəli', 'Xeyr')
    bot.reply_to(message, "Bu mesajı anonim göndərmək istəyirsinizmi? (bəli və ya xeyr)", reply_markup=markup)

    # Check if the user wants to send the message anonymously
    bot.register_next_step_handler(message, lambda message: ask_anonymous(message, message_text))
    

# Start the bot
bot.polling()
