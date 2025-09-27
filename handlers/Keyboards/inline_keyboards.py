from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.Dialogs.dialogs import PERSONS

def main_menu():
    Menu_List=[
        [
            InlineKeyboardButton(text='Информация о нас', callback_data='Information about us'),
            InlineKeyboardButton(text="Наш сайт", url='https://decortime.pro/'),
            InlineKeyboardButton(text="Расчет кол-во Штукатурки, Лака и Грунтовки", callback_data='paint calculation')
        ],
        [
            InlineKeyboardButton(text="Игра|Qwize", callback_data='Quiz_game'),
            InlineKeyboardButton(text="Диалог с личностью", callback_data='Dialogue_with_the_individual'),
            InlineKeyboardButton(text="Факты",callback_data='Facts')
        ],
        [
            InlineKeyboardButton(text="Рекоминдации по фильмам", callback_data="Recommendations_move"),
            InlineKeyboardButton(text="Переводчик", callback_data="Translator")
        ]
    ]
    keyboard=InlineKeyboardMarkup(inline_keyboard=Menu_List)
    return keyboard

def info_company():
    info_list=[
        [
            InlineKeyboardButton(text="Главный офис",callback_data='Locations'),
            InlineKeyboardButton(text="Наши магазины", callback_data='stors')
        ]
    ]
    keyboard=InlineKeyboardMarkup(inline_keyboard=info_list)
    return keyboard


def Twinstor_stors():
    Twinstor_list=[
        [
            InlineKeyboardButton(text="Галерея интерьеров «Твинстор",callback_data='Twinstor')
        ]

    ]
    keyboard=InlineKeyboardMarkup(inline_keyboard=Twinstor_list)
    return keyboard


def paint_choice():
    Paint_Choise=[
        [
            InlineKeyboardButton(text='Грунт Adhesive ', callback_data='adhesive'),
            InlineKeyboardButton(text='Штукатурка GRANELLA ', callback_data='granella'),
            InlineKeyboardButton(text='Лак КRAFT PRO MATT ', callback_data='kraft_pro_matt'),
            InlineKeyboardButton(text='Лак Durata ', callback_data='durata')
        ]
    ]
    keyboard=InlineKeyboardMarkup(inline_keyboard=Paint_Choise)
    return keyboard


def paint_calculate():
    paint_calculate=[
        [
            InlineKeyboardButton(text="Рассчет штукатурки", callback_data='plaster'),
            InlineKeyboardButton(text="Рассчет лака", callback_data='varnish'),
            InlineKeyboardButton(text="Рассчет грунтовки", callback_data='primers')
        ]
     ]
    keyboard=InlineKeyboardMarkup(inline_keyboard=paint_calculate)
    return keyboard

def store_information():
    store_information=[
        [
            InlineKeyboardButton(text="Галерея интерьеров «Твинстор", callback_data='Twinstor')
        ]
    ]
    keyboard=InlineKeyboardMarkup(inline_keyboard=store_information)
    return keyboard


def another_fact():
    another_list=[
         [
            InlineKeyboardButton(text="Еще один факт", callback_data='again_fact')
         ]
    ]
    keyboard=InlineKeyboardMarkup(inline_keyboard=another_list)
    return keyboard


def get_persons_keyboard():
    persons_list=InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=name,callback_data=f'select_persons:{name}')
        ]
        for name in PERSONS
    ]
    )
    return persons_list


def close():
    Close_list=InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Закончить',callback_data='close')
        ]
    ])

    return Close_list


def topic_keyboard():
    topic = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Машины', callback_data='topic:car')],
            [InlineKeyboardButton(text='Оружие', callback_data='topic:weapons')],
            [InlineKeyboardButton(text='IT', callback_data='topic:it')],
        ]
    )
    return topic


def quiz_answers():
    Quiz_List = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Еще вопрос', callback_data='next_question')],
            [InlineKeyboardButton(text='Сменить тему', callback_data='change_topic')],
            [InlineKeyboardButton(text='Закончить', callback_data='end_quiz')],
        ]
    )
    return Quiz_List


def movie_menu():
    Move_list=InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Ужасы', callback_data='films:horror')],
            [InlineKeyboardButton(text='Комедия', callback_data='films:comedy')],
            [InlineKeyboardButton(text='Боевик', callback_data='films:action')],
        ]
    )
    return Move_list


def recommendation_move():
    Recommendation_List = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Не нравится', callback_data='dislike_recommendation')],
            [InlineKeyboardButton(text='Сменить жанр', callback_data='change_genre')],
            [InlineKeyboardButton(text='Закончить', callback_data='end_recommendations')],
        ]
    )
    return Recommendation_List


def languages_menu():
    languages_list=InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Английский', callback_data='languages_English')],
            [InlineKeyboardButton(text='Татарский', callback_data='languages_Tatar')],
            [InlineKeyboardButton(text='Немецкий', callback_data='languages_Deutsch')],
        ]
    )
    return languages_list


def translation_keyboard():
    translation_list=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=" Сменить язык", callback_data="change_language")],
        [InlineKeyboardButton(text=" Закончить", callback_data="translator_end")]
    ]
    )
    return translation_list