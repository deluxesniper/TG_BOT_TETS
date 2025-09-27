from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from handlers.Dialogs.dialogs import PERSONS, dialogis
from handlers.Keyboards.inline_keyboards import get_persons_keyboard
from handlers.States.dialogue_with_an_unknown_person import MessagesPersona

router=Router()

@router.callback_query(F.data=="Dialogue_with_the_individual")
async def talk_dialog(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Диалог с известной личностью",reply_markup=get_persons_keyboard())


@router.callback_query(F.data.startswith('select_persons:'))
async def select_persons_handler(call: CallbackQuery,state: FSMContext):
    select_persons=call.data.split(":")[-1]
    dialogis[call.from_user.id] = {
        'persona': PERSONS[select_persons],
        'messages': []
    }
    print(dialogis)
    await call.message.answer(f'Ты выбрал {select_persons}. Можешь пообщаться с ним')
    await state.set_state(MessagesPersona.message)


@router.callback_query(F.data.startswith('close'))
async def close_handler(call: CallbackQuery, state: FSMContext):
    await state.clear()