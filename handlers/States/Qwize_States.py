from aiogram import Router
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from handlers.Keyboards.inline_keyboards import quiz_answers
from handlers.Qwize.Qwize_games import check_answer, get_score, increase_score

router = Router()


class QuizStates(StatesGroup):
    choosing_topic = State()
    waiting_answer = State()


@router.message(QuizStates.waiting_answer)
async def waiting_answer_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    question = data.get('question')
    result = await check_answer(question, message.text)
    await message.answer('Сейчас дам ответ')
    if result == 'правильно':
        score = await increase_score(state)
        await message.answer(f'✅ Правильно, твой счет {score}',reply_markup=quiz_answers())
    else:
        score = await get_score(state)
        await message.answer(f'⛔️ Неправильно твой счет {score}', reply_markup=quiz_answers())


