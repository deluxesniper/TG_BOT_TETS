from aiogram import Router
from aiogram.fsm.state import State,StatesGroup


router=Router()

class TranslationStates(StatesGroup):
    waiting_for_text = State()
    waiting_for_language = State()