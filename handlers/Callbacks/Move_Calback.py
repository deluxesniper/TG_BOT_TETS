from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from handlers.Keyboards.inline_keyboards import movie_menu, recommendation_move
from handlers.Move.move_recomindation import recommendations_move
from handlers.States.Move_States import Move

router = Router()


@router.callback_query(F.data == 'Recommendations_move')
async def genre_handler( call:CallbackQuery):
    await call.message.answer('Выбери Жанр', reply_markup=movie_menu())
    await call.answer()

@router.callback_query(F.data.startswith('films:'))
async def movie_handler(call: CallbackQuery, state: FSMContext):
    rem = call.data.split(":")[-1]
    await call.answer('Сейчас подскажу 5 лучших фильмов по жанру', show_alert=True)
    films= await recommendations_move(rem)
    await state.update_data(films=films)
    await state.set_state(Move.feedback_waiting)
    await call.message.answer(f'🎬 Рекомендации по жанру "{rem}":\n\n{films}',reply_markup=recommendation_move())


@router.callback_query(F.data == 'dislike_recommendation')
async def dislike_recommendation_handler(call: CallbackQuery, state: FSMContext):
    await call.answer('Ищу другие варианты...', show_alert=True)
    data = await state.get_data()
    genre = data.get('films')
    new_recommendations = await recommendations_move(genre)
    await call.message.edit_text(f'🎬 Новые рекомендации по жанру "{genre}":\n\n{new_recommendations}',reply_markup=recommendation_move())


@router.callback_query(F.data == 'change_genre')
async def change_genre_handler(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.answer('Выбери новый жанр фильмов', reply_markup=movie_menu())

@router.callback_query(F.data == 'end_recommendations')
async def end_recommendations_handler(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.answer('🎬 Рекомендации завершены! Надеюсь, ты нашел что-то интересное!')


