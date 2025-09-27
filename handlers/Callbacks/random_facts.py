from aiogram import Router
from aiogram import F
from aiogram.types import CallbackQuery
from handlers.Keyboards.inline_keyboards import another_fact
from  handlers.Random__fact.Random_fact import random_fact


router=Router()


@router.callback_query(F.data =="Facts")
async def random_handler(call:CallbackQuery):
    await call.answer('Щас расскажу как появились краски, каждая история отличается от другой',show_alert=True)
    fact = await random_fact()
    await call.message.answer(f'Факт: {fact}',reply_markup=another_fact())