from aiogram import Router
from aiogram.fsm.state import State ,StatesGroup
router=Router()


class Move(StatesGroup):
   feedback_waiting= State()

