from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram.types import Message
from handlers.Keyboards.inline_keyboards import languages_menu, translation_keyboard
from handlers.States.Languages_State import TranslationStates
from handlers.Translations.translator import user_translations

router=Router()


@router.callback_query(F.data=='Translator')
async def translate_text(call:CallbackQuery,state:FSMContext):
    await call.answer()
    await state.set_state(TranslationStates.waiting_for_language)
    await call.message.answer('Выбирите язык для перевода',reply_markup=languages_menu())


@router.callback_query(F.data=="languages_English")
async def languages(call:CallbackQuery,state:FSMContext):
    await state.update_data(language='Английский')
    await state.set_state(TranslationStates.waiting_for_text)
    await call.message.edit_text("Выбран Английский , отправте ваш текст",reply_markup=translation_keyboard())


@router.callback_query(F.data == "languages_Tatar")
async def languages(call: CallbackQuery, state: FSMContext):
    await state.update_data(language='Татарский')
    await state.set_state(TranslationStates.waiting_for_text)
    await call.message.edit_text("Выбран Татарский , отправте ваш текст", reply_markup=translation_keyboard())


@router.callback_query(F.data == "languages_Deutsch")
async def languages(call: CallbackQuery, state: FSMContext):
        await state.update_data(language='Немецкий')
        await state.set_state(TranslationStates.waiting_for_text)
        await call.message.edit_text("Выбран Немецкий , отправте ваш текст", reply_markup=translation_keyboard())


@router.message(TranslationStates.waiting_for_text,F.text)
async def translation_user(message:Message, state: FSMContext):
    user_data = await state.get_data()
    language = user_data['language']
    original_language = message.text
    translated_text = await user_translations(original_language, language)

    await message.answer(
        f"🌍 <b>Перевод на {language}:</b>\n\n"
        f"📌 <b>Оригинал:</b>\n{original_language}\n\n"
        f"🔤 <b>Перевод:</b>\n{translated_text}",
        reply_markup=translation_keyboard()
    )


@router.callback_query(F.data == "change_language")
async def change_language(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        "🌍 Выберите язык для перевода:",
        reply_markup=languages_menu()
    )

# Завершение
@router.callback_query(F.data == "translator_end")
async def end_translator(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    from handlers.Keyboards.inline_keyboards import main_menu
    await callback.message.edit_text(
        "✅ Переводчик завершил работу.",
        reply_markup=main_menu()
    )