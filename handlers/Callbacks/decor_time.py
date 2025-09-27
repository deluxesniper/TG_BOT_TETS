from aiogram import Router,F
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton,Message
from aiogram.fsm.context import FSMContext
from handlers.States.calculation_paints import Calcs_adhesive,Calcs_Durata,Calcs_granella,Calcs_kraft_pro_matt
from handlers.Keyboards.inline_keyboards import main_menu, paint_calculate, paint_choice, store_information, \
    info_company, Twinstor_stors
from handlers.addresses import XL_address,XL_city,XL_email,XL_phone,XL_opening_hours


router=Router()


@router.callback_query(F.data=="paint calculation")
async def paint_to_calculate_handler(call: CallbackQuery):
    await call.answer()
    await call.message.answer("Вы хотите рассчитать количество не обходимой объёма краски, лака или грунтовки, тогда выберите нужную",reply_markup=paint_choice())


@router.callback_query(F.data=="adhesive")
async def calculate_Priming_Adhesive_handler(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Введите площадь помещения в м²")
    await state.set_state(Calcs_adhesive.waiting)
    await call.answer()


@router.message(Calcs_adhesive.waiting)
async def formula_adhesive(message: Message, state: FSMContext):
            adhesive = float(message.text)
            adhesive_consumption = 7.5
            result = adhesive / adhesive_consumption

            await message.answer(
                f"С вашей площадью {adhesive} м²\n"
                f"Вам потребуется: {result:.2f} литров грунтовки Adhesive\n"
                f"Расход: {adhesive_consumption} м²/литр"
            )
            await state.clear()


@router.callback_query(F.data=="granella")
async def calculate_plaster_handler(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Введите площадь помещения в м²")
    await state.set_state(Calcs_granella.waiting)
    await call.answer()


@router.message(Calcs_granella.waiting)
async def formula_granella(message: Message, state: FSMContext):
    granella = float(message.text)
    granella_consumption = 4
    result = granella / granella_consumption
    await message.answer(f"С вашей площадью {granella} м²\n Вам потребуется: {result:.2f} литров штукатурки Granella\n Расход: {granella_consumption} м²/литр")
    await state.clear()


@router.callback_query(F.data=="kraft_pro_matt")
async def calculate_varnish_handler(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Введите площадь помещения в м²")
    await state.set_state(Calcs_kraft_pro_matt.waiting)
    await call.answer()


@router.message(Calcs_kraft_pro_matt.waiting)
async def formula_kraft_pro_matt(message: Message, state: FSMContext):
    kraft_pro_matt = float(message.text)
    kraft_pro_matt_consumption = 10
    result = kraft_pro_matt / kraft_pro_matt_consumption
    await message.answer(f"С вашей площадью {kraft_pro_matt} м²\n Вам потребуется: {result:.2f} литров  лака Kraft pro matt\n Расход: {kraft_pro_matt_consumption} м²/литр")
    await state.clear()


@router.callback_query(F.data=="durata")
async def calculate_varnish_handler(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Введите площадь помещения в м²")
    await state.set_state(Calcs_Durata.waiting)
    await call.answer()


@router.message(Calcs_Durata.waiting)
async def formula_durata(message: Message, state: FSMContext):
    durata = float(message.text)
    durata_consumption = 10
    result = durata / durata_consumption
    await message.answer(f"С вашей площадью {durata} м²\n Вам потребуется: {result:.2f} литров  лака Durata\n Расход: {durata_consumption} м²/литр")
    await state.clear()


@router.callback_query(F.data=="Information about us")
async def info(call:CallbackQuery):
    await call.answer()
    await call.message.answer("Вы выбрали информацию о нас, выберите что хотите знать",reply_markup=info_company())



@router.callback_query(F.data =="Locations")
async def location(call:CallbackQuery):
    await  call.answer()
    await call.message.answer(f"Наш адрес: {XL_city} {XL_address}\n время работы: {XL_opening_hours}\n телефон: {XL_phone}\n EMAIL@: {XL_email}")



@router.callback_query(F.data =="stors")
async def stors(call:CallbackQuery):
    await call.answer()
    await call.message.answer("Адреса наших магазинов",reply_markup=Twinstor_stors())