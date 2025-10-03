from pyrogram import Client, filters
import datetime
import keyboards
import random
import json
from pyrogram import emoji
from FushionBrainAI import generate
import base64
from pyrogram.types import ForceReply
rps_answers = ['Камень', 'Ножницы', 'Бумага']
query_contact_text = "Введите сообщения для создателя бота:"

bot = Client(
    api_id=2040,
    api_hash='b18441a1ff607e10a989891a5462e627',
    bot_token='7092071196:AAFSauf87-U6KkyThD4jhvyYpv1yNVYEKQw',
    name='mrleniks_bot'

)
# FushionBrain
API_KEY = "A95C7130AB56D0D9D469010E9C49F433"
SECRET_KEY = "FBB07EC1D52819309848CE7C88D3D0CE"


def button_filter(button):
    async def func(_, __, msg):
        return msg.text == button.text

    return filters.create(func, "ButtonFilter", button=button)


@bot.on_message(filters.command("start"))
async def start(bot, message):

    print(message.chat.id)
    await message.reply("Добро пожаловать!",
                        reply_markup=keyboards.kb_main)
    with open("users.json", "r") as file:
        users = json.load(file)
    with open("quest_users.json", "r") as file:
        quest_users = json.load(file)

    if str(message.from_user.username) not in users.keys():
        users[message.from_user.username] = 50

    with open("users.json", "w") as file:
        json.dump(users, file)
    if str(message.from_user.username) not in quest_users.keys():
        quest_users[message.from_user.username] = 0
    with open("quest_users.json", "w") as file:
        json.dump(quest_users, file)
    await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEMwa5m1xAEYYN2PD8fx9W0373m8eJL-AACIEsAAq4cSUhFIkR8EbluyDUE")


@bot.on_message(filters.command("programmer"))
async def programmer(bot, message):
    await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEMwaxm1w_rWwitkq9VfbJeiM4fu3P63gACSkYAAjI5UEjOMrjdNrjbETUE")


@bot.on_message(filters.command("info") | button_filter(keyboards.btn_info))
async def info(bot, message):
    await bot.send_message(message.chat.id,
                           "/start - Запустить бота                                                                                                                                                   /time - Узнать текущую дату и время                                                                                    /info - Отправить список всех комманд                                                                                                /programmer - Узнать программист ли ты?                                                                                      ")


@bot.on_message(filters.command("time") | button_filter(keyboards.btn_time))
async def time(bot, message):
    await bot.send_message(message.chat.id,
                           f"Текущая дата: {datetime.datetime.now().date()}. Текущее время: {datetime.datetime.now().time()}")


@bot.on_message(button_filter(keyboards.btn_games))
async def games(bot, message):
    await message.reply("Хорошо! Выберите игру",
                        reply_markup=keyboards.kb_games
                        )


@bot.on_message(button_filter(keyboards.btn_rockpaperscissors))
async def rockpaperscissors_hub(bot, message):
    await bot.send_message(message.chat.id, f"Игра: Камень-Ножницы-Бумага",
                           reply_markup=keyboards.kb_rps_hub
                           )


@bot.on_message(button_filter(keyboards.btn_rps_play))
async def rockpaperscissors(bot, message):
    await bot.send_message(message.chat.id, f"Тогда давайте играть!",
                           reply_markup=keyboards.kb_rockpaperscissors
                           )


@bot.on_message(button_filter(keyboards.btn_back))
async def back(bot, message):
    await bot.send_message(message.chat.id, f"Меню",
                           reply_markup=keyboards.kb_main
                           )


@bot.on_message(
    button_filter(keyboards.btn_stone) | button_filter(keyboards.btn_paper) | button_filter(keyboards.btn_scissors))
async def choice_rps(bot, message):
    with open("users.json", "r") as file:
        users = json.load(file)
    rock = keyboards.btn_stone.text
    paper = keyboards.btn_paper.text
    scissors = keyboards.btn_scissors.text
    user = message.text
    bot = random.choice([rock, paper, scissors])

    if user == bot:
        await message.reply("Ничья")
    elif (user == rock and bot == scissors) or (user == paper and bot == rock) or (user == scissors and bot == paper):
        await message.reply(f"Ты выйграл. бот выбрал{bot}", reply_markup=keyboards.kb_games)
        users[message.from_user.username] += 10
    else:
        await message.reply(f"Ты проиграл. Бот выбрал{bot}", reply_markup=keyboards.kb_games)
        users[message.from_user.username] += -10
    with open("users.json", "w") as file:
        json.dump(users, file)

@bot.on_message(filters.command("quest") | button_filter(keyboards.btn_quest))
async def quest(bot, message,):
    await message.reply_text(f"Вы уверены?{emoji.SKULL}", reply_markup=keyboards.inline_kb_start_quest)
@bot.on_message(button_filter(keyboards.btn_leaderboard))
async def leaderboard_rps(bot, message):
    with open("users.json", "r") as file:
        users = json.load(file)
    users = dict(sorted(users.items()))
    for title, text in users.items():
        await bot.send_message(message.chat.id, f"{title} : {text}")
@bot.on_callback_query()
async def handle_quest_query(bot, query):
    with open("quest_users.json", "r") as file:
        quest_users = json.load(file)
    await  query.message.delete()
    await bot.answer_callback_query(query.id, text="Добро пожаловать на квест под названием По дороге домой", show_alert=True)
    if query.data == 'start_quest':
        await query.message.reply_text("Вы идете по темному переулку. Тут вы замечаете что за вами идет человек в черном")
        await query.message.reply_text("Что будете делать?", reply_markup=keyboards.kb_inline_quest_nothing)
    if query.data == 'quest_nothing':
        await query.message.reply_text("Вы ничего не делали и резко получили сиьлный удар в голову, вы очнулись и поняли что связаны и ослеплены мешком на голове")
    if query.data == 'quest_faster':
        await query.message.reply_text("Вы ускорили шаг и услышали что незнокомец тоже ускорился, вы перешли на бег и он за вами. Адреналин в крови сильно поднялся")
        await query.message.reply_text("Что будете делать?", reply_markup=keyboards.kb_inline_quest_second)
    if query.data == 'runaway':
        await query.message.reply_text("Вы начали бежать но споткнулись, и не успев поднятся получили сильный удар в голову, очнулись вы уже связаные и с мешком на голове")
    if query.data == 'try_to_fight':
        await query.message.reply_text("Вы резко обернулись и после недолгой борьбы повалили его наспину")
        quest_users[query.message.from_user.username] += 1
@bot.on_message(filters.command('image'))
async def image(bot, message):
    if len(message.text.split()) > 1:
        query = message.text.replace('/image', '')
        await message.reply_text(f'Генерирую изображение по запросу **{query}** Ожидание около минуты')
        images = await generate(query)
        if images:
            image_data = base64.b64decode(images[0])
            img_num = random.randint(0, 99)
            with open(f"images/image{img_num}.jpg", "wb") as file:
                file.write(image_data)
                await bot.send_photo(message.chat.id, f'images/image{img_num}.jpg', reply_to_message_id=message.id, reply_markup=keyboards.kb_main)
        else:
            await message.reply_text(f"Возникла ошибка! Попробуйте еще раз", reply_to_message_id=message.id, reply_markup=keyboards.kb_main)
    else:
        bot.send_message(message.chat.id, "Комманда должна выглядеть так - /image Запрос")
query_text = "Введи запрос для генерации изображения"
@bot.on_message(button_filter(keyboards.btn_image_generate))
async def button_generate_image(bot, message):
    await bot.send_message(message.chat.id, query_text, reply_markup=ForceReply(True))
@bot.on_message(filters.command("contact"))
async def contact(bot, message):
    await bot.send_message(message.chat.id, query_contact_text, reply_markup=ForceReply(True))
@bot.on_message(button_filter(keyboards.btn_image_generate))
async def button_generate_image(bot, message):
    await bot.send_message(message.chat.id, query_text, reply_markup=ForceReply(True))

@bot.on_message(filters.command("contact") | button_filter(keyboards.btn_support))
async def contact(bot, message):
    await bot.send_message(message.chat.id, query_contact_text, reply_markup=ForceReply(True))
#@bot.on_message(filters.reply & filters.user(5988340652))
#async def respond_to_user(client, message):
#    if message.reply_to_message:
#        target_user_id = int(message.reply_to_message.text.split('P.S - ')[-1])
#        await client.send_message(
 #           target_user_id,
 #           f"Ответ администратора:\n{message.text}"
#        )
@bot.on_message(filters.reply)
async def replies(bot, message):
    user = message.from_user
    if message.reply_to_message.text == query_contact_text:
        await bot.send_message(
            5988340652,
            f"Новое сообщение от {user.first_name} (@{user.username}):\n{message.text}\n\nP.S - {user.id}",  reply_markup=keyboards.kb_main)
        #await bot.send_message(5988340652, f"Ответить пользователю {user.first_name}", reply_markup=ForceReply(True))
        print("Message to Admin sent")

    elif message.reply_to_message.text == query_text:
        query = message.text
        await bot.send_message(message.chat.id, f"Генерирую изображение по запросу **{query}** Ожидание около минуты")
        assert isinstance(query, object)
        images = await generate(query)
        if images:
            image_data = base64.b64decode(images[0])
            img_num = random.randint(0, 99)
            with open(f'images/image{img_num}.jpg', 'wb') as file:
                file.write(image_data)
                await bot.send_photo(message.chat.id, f'images/image{img_num}.jpg', reply_to_message_id=message.id, reply_markup=keyboards.kb_main)
        else:
            await message.reply_text(f"Возникла ошибка! Попробуйте еще раз", reply_to_message_id=message.id, reply_markup=keyboards.kb_main)
    #elif message.reply_to_message.text == f"Ответить пользователю {user.first_name}":
    #    target_user_id = int(message.reply_to_message.text.split('P.S - ')[-1])
    #    await bot.send_message(
    #        target_user_id,
    #        f"Ответ администратора:\n{message.text}"
    #    )

@bot.on_message(button_filter(keyboards.btn_profile))
async def Profile(bot, message):
    user = message.from_user
    with open("users.json", "r") as file:
        users = json.load(file)
    with open("quest_users.json", "r") as file:
        quest_users = json.load(file)
    title = users[message.from_user.username]
    users = dict(sorted(users.items()))
    await bot.send_message(message.chat.id, f"Вы: Ваше имя:{user.first_name}(@{user.username}) Ваши очки в Камень-ножницы-бумага: {users[message.from_user.username]} Количество побед в квесте {quest_users[message.from_user.username]}", reply_markup=keyboards.kb_main)
bot.run()