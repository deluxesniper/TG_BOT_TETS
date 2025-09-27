from aiogram import Router
from handlers.Callbacks.decor_time import router as decor_time_router
from handlers.Commands import router as commands_router
from handlers.Callbacks.random_facts import router as random_facts
from handlers.Callbacks.dialogs_callback import router as dialogs_router
from handlers.Callbacks.Qwize_callback import router as qwize_callback
from handlers.Qwize.Qwize_games import router as Qwize_games_router
from handlers.States.Qwize_States import router as states_router
from handlers.Move.move_recomindation import router as move_recomindation_router
from handlers.States.Move_States import router as move_state_router
from handlers.Callbacks.Move_Calback import router as move_calback_router
from handlers.Callbacks.languages_callback import router as languages_router
from handlers.Translations.translator import router as translator
from handlers.States.Languages_State import router as languages_state_router
from handlers.Callbacks.Move_Calback import router as move_calback_router
from handlers.Keyboards.reply_keyboards import router as reply_keyboards
from handlers.States.create_a_message_for_the_user import router as create_a_message_for_the_user_router
from handlers.Callbacks.MEssages_Call import router as messages_call
router = Router()


router.include_routers(commands_router,decor_time_router,random_facts,
                       dialogs_router, qwize_callback,Qwize_games_router,
                       states_router,move_state_router,move_recomindation_router,
                       move_calback_router, languages_router,translator,languages_state_router,reply_keyboards,create_a_message_for_the_user_router,messages_call)
