from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from handlers.Keyboards.inline_keyboards import topic_keyboard
from handlers.Qwize.Qwize_games import get_quiz_question, get_score
from handlers.States.Qwize_States import QuizStates


router = Router()


@router.callback_query(F.data=="Quiz_game")
async def qwize_handler( call:CallbackQuery):
    await call.message.answer('Выбери тему для квиза', reply_markup=topic_keyboard())
    await call.answer()


@router.callback_query(F.data.startswith('topic:'))
async def close_mode_handler(call: CallbackQuery, state: FSMContext):
    await call.answer('Сейчас задам вопрос', show_alert=True)
    topic = call.data.split(':')[-1]
    question = await get_quiz_question(topic)
    await state.update_data(question=question)
    await state.update_data(topic=topic)
    await state.set_state(QuizStates.waiting_answer)
    await call.message.answer(f'Тема: {topic}\n\n{question}\n Можешь ответить на вопрос.')


@router.callback_query(F.data == 'next_question')
async def next_quiz_qestion_handler(call: CallbackQuery, state: FSMContext):
    await call.answer('Сейчас задам вопрос', show_alert=True)
    data = await state.get_data()
    topic = data.get('topic')
    question = await get_quiz_question(topic)
    await call.message.answer(f'Продолжаем по теме: {topic}\n\n{question}')
    await state.set_state(QuizStates.waiting_answer)


@router.callback_query(F.data == 'change_topic')
async def next_quiz_question_handler(call: CallbackQuery):
    await call.message.answer('Выбери новую тему', reply_markup=topic_keyboard())


@router.callback_query(F.data == 'end_quiz')
async def next_quiz_qestion_handler(call: CallbackQuery, state: FSMContext):
    score = await get_score(state)
    await state.clear()
    await call.message.answer(f'🎬 Квиз завершен! Твйо итоговый счет: {score}')
