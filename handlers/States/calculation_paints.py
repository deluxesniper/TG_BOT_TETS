from aiogram import Router
from aiogram.fsm.state import State,StatesGroup

router=Router()


class Calcs_adhesive(StatesGroup):
    waiting = State()


class Calcs_granella(StatesGroup):
    waiting = State()


class Calcs_kraft_pro_matt(StatesGroup):
    waiting = State()


class Calcs_Durata(StatesGroup):
    waiting = State()