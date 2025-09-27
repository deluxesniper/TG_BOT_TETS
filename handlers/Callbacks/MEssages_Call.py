from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from handlers.Keyboards.reply_keyboards import under_the_menu, save_or_clear
from handlers.States.create_a_message_for_the_user import Сreate_a_message_for_the_user
from handlers.to_json import save_message, load_messages

router=Router()

@router.message(F.text == "Объявления")
async def menu_handler(message: Message):
    await message.answer("Что хотите сделать: создать или просмотреть ваши объявления",reply_markup=under_the_menu())



@router.message(F.text =="Создать Объявление")
async def zagolovok(message: Message,state: FSMContext):
    await state.set_state(Сreate_a_message_for_the_user.user_message)
    await message.answer( "Отлично! Давайте создадим объявление.\n\n"
        "📌 Шаг 1 из 6: Введите заголовок объявления:")




@router.message(Сreate_a_message_for_the_user.user_message,F.text)
async def create_user_handler(message: Message,state: FSMContext):
    await state.update_data(user_for_text=message.text)
    await state.set_state(Сreate_a_message_for_the_user.name)
    await message.answer("📝 Шаг 2 из 6: напишите ваше имя:" )


@router.message(Сreate_a_message_for_the_user.name,F.text)
async def create_name_handler(message: Message,state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Сreate_a_message_for_the_user.age)
    await  message.answer("📝Шаг 3 из 6: напишите ваш возраст ")



@router.message(Сreate_a_message_for_the_user.age,F.text)
async def create_age_handler(message: Message,state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Сreate_a_message_for_the_user.city)
    await  message.answer("📝Шаг 4 из 6: напишите ваш город ")


@router.message(Сreate_a_message_for_the_user.city,F.text)
async def create_city_handler(message: Message,state: FSMContext):
    await state.update_data(city=message.text)
    await state.set_state(Сreate_a_message_for_the_user.user_advertisement)
    await message.answer("📝Шаг 5 из 6: напишите текст объявления")




@router.message(Сreate_a_message_for_the_user.user_advertisement, F.text)
async def create_announcement_handler(message: Message, state: FSMContext):
    await state.update_data(announcement=message.text)  # ✅
    await state.set_state(Сreate_a_message_for_the_user.price)
    await message.answer("📝 Шаг 6 из 6: напишите вашу цену")


@router.message(Сreate_a_message_for_the_user.price, F.text)
async def create_payment_handler(message: Message, state: FSMContext):
    await state.update_data(payment=message.text)
    data = await state.get_data()

    preview_text = (
        "📋 Предпросмотр объявления:\n\n"
        f"📌 Заголовок: {data.get('user_for_text')}\n"
        f"👤 Имя: {data.get('name')}\n"
        f"🎂 Возраст: {data.get('age')}\n"
        f"🏙️ Город: {data.get('city')}\n"
        f"📝 Текст: {data.get('announcement')}\n"
        f"💰 Цена: {data.get('payment',)}\n\n"
        "Выберите действие:"
    )

    await state.set_state(Сreate_a_message_for_the_user.user_confirmation)
    await message.answer(preview_text, reply_markup=save_or_clear())


@router.message(Сreate_a_message_for_the_user.user_confirmation, F.text.in_(["Сохранить", "Не сохранять"]))
async def handle_confirmation(message: Message, state: FSMContext):
    if message.text == "Сохранить":
        data = await state.get_data()
        message_data = {
            "user_for_text": data.get('user_for_text', 'Не указано'),
            "name": data.get('name'),
            "age": data.get('age'),
            "city": data.get('city'),
            "announcement": data.get('announcement'),
            "payment": data.get('payment')

        }
        save_message(message_data)
        await message.answer("✅ Объявление успешно сохранено!", reply_markup=under_the_menu())
    else:
        await message.answer("❌ Создание объявления отменено.", reply_markup=under_the_menu())

    await state.clear()


@router.message(Сreate_a_message_for_the_user.user_confirmation)
async def handle_invalid_confirmation(message: Message, state: FSMContext):
    await message.answer("Пожалуйста, выберите действие с помощью кнопок:", reply_markup=save_or_clear())


@router.message(F.text == "Мои Объявления")
async def show_my_advertisements(message: Message):
    advertisements = load_messages()

    if not advertisements:
        await message.answer("У вас пока нет сохраненных объявлений.", reply_markup=under_the_menu())
        return

    # Показываем все объявления
    for i, ad in enumerate(advertisements, 1):
        ad_text = (
                f"📋 Объявление #{i}\n\n"
                f"📌 Заголовок: {ad.get('user_for_text', 'Не указано')}\n"
                f"👤 Имя: {ad.get('name', 'Не указано')}\n"
                f"🎂 Возраст: {ad.get('age', 'Не указано')}\n"
                f"🏙️ Город: {ad.get('city', 'Не указано')}\n"
                f"📝 Текст объявления: {ad.get('announcement', 'Не указано')}\n"
                f"💰 Цена: {ad.get('payment', 'Не указано')}\n"

        )
        await message.answer(ad_text)

    await message.answer(f"📊 Всего объявлений: {len(advertisements)}", reply_markup=under_the_menu())
