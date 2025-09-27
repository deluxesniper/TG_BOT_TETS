from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from handlers.Keyboards.inline_keyboards import main_menu
from handlers.Keyboards.reply_keyboards import menu

router=Router()


@router.message(Command('start'))
async def start(message: Message):
    await message.answer(f"""Здравствуйте! {message.from_user.full_name} \nВас приветствует компания ООО «ДекорТайм»\nОфициальный дистрибьютор производителей декоративных покрытий:
Cebos Color, Valpaint, San Marco, Ticiana Deluxe, Werth Deco и представитель лакокрасочной продукции Flugger.\n\nМожете ознакомиться с моими функциями ниже""", reply_markup=main_menu())



@router.message(Command('add'))
async def add(message: Message):
    await message.answer(f"Здравствуйте! {message.from_user.full_name} хотите создать обьявление?", reply_markup=menu())

