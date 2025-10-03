from pyrogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import emoji

btn_info = KeyboardButton(f"{emoji.INFORMATION} Инфо")
btn_games = KeyboardButton(f"{emoji.VIDEO_GAME} Игры")
btn_profile = KeyboardButton(f"{emoji.PERSON} Профиль")
btn_back = KeyboardButton(f'{emoji.BACK_ARROW} Назад')
btn_stone = KeyboardButton(f"{emoji.ROCK} Камень")
btn_paper = KeyboardButton(f"{emoji.PAPERCLIP} Бумага")
btn_scissors = KeyboardButton(f"{emoji.SCISSORS} Ножницы")
btn_rockpaperscissors = KeyboardButton(f"{emoji.VIDEO_GAME} Камень-ножницы-бумага")
btn_quest = KeyboardButton(f"{emoji.CITYSCAPE_AT_DUSK} Квест")
btn_time = KeyboardButton(f"{emoji.TIMER_CLOCK} Время")
btn_leaderboard = KeyboardButton(f"{emoji.FIRST_PLACE_MEDAL} Таблица лидеров")
btn_rps_play = KeyboardButton(f"{emoji.PLAY_BUTTON} Играть")
btn_image_generate = KeyboardButton(f"{emoji.PAINTBRUSH} Сгенерировать изображение")
btn_support = KeyboardButton(f"{emoji.CALL_ME_HAND} Поддержка")

btn_inline_quest = InlineKeyboardButton(f'{emoji.CITYSCAPE} Пройти квест', callback_data='start_quest')
btn_inline_quest_nothing = InlineKeyboardButton('Ничего не делать, он просто попути', callback_data='quest_nothing')
btn_inline_quest_faster = InlineKeyboardButton(f'{emoji.FAST_UP_BUTTON} Ускорить шаг', callback_data='quest_faster')
btn_inline_quest_try_to_fight = InlineKeyboardButton(f'{emoji.RAISED_FIST} Попробовать напасть', callback_data='quest_try_to_fight')
btn_inline_quest_run_to_humans = InlineKeyboardButton(f"{emoji.MAN_RUNNING} Бежать к полиции", callback_data='runaway')
btn_inline_quest_play_again = InlineKeyboardButton(f"{emoji.REVERSE_BUTTON} Сыграть еще раз")

kb_main = ReplyKeyboardMarkup(
                keyboard=[
                    [btn_info, btn_games, btn_profile, btn_time],
                    [btn_image_generate, btn_support]
                ],
                resize_keyboard=True
            )
kb_rockpaperscissors = ReplyKeyboardMarkup(
    keyboard=[
        [btn_stone, btn_scissors, btn_paper],
        [btn_back]
    ],
    resize_keyboard=True
)
kb_games = ReplyKeyboardMarkup(
    keyboard=[
        [btn_rockpaperscissors, btn_quest],
        [btn_back]
    ],
    resize_keyboard=True
)
kb_rps_hub = ReplyKeyboardMarkup(
    keyboard=[
        [btn_leaderboard, btn_rps_play],
        [btn_back]
    ],
    resize_keyboard=True
)
inline_kb_start_quest = InlineKeyboardMarkup([
    [btn_inline_quest]
])
kb_inline_quest_nothing = InlineKeyboardMarkup([
    [btn_inline_quest_nothing, btn_inline_quest_faster]
])
kb_inline_quest_second = InlineKeyboardMarkup([
    [btn_inline_quest_try_to_fight, btn_inline_quest_run_to_humans]
])
kb_inline_quest_play_again = InlineKeyboardButton([
    [btn_inline_quest_play_again]
])