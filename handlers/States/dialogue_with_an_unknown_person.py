from aiogram.fsm.state import StatesGroup,State
from aiogram import Router


router = Router()

class MessagesPersona(StatesGroup):
    message = State()
