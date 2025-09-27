from aiogram.fsm.state import StatesGroup,State
from aiogram import Router

router = Router()

class Сreate_a_message_for_the_user(StatesGroup):
    user_message=State()
    name=State()
    age=State()
    city=State()
    user_advertisement=State()
    price=State()
    user_confirmation=State()