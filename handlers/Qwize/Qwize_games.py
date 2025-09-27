from aiogram import Router
from openai import AsyncOpenAI
from handlers.Config.configs import OpenAI_KEY
from aiogram.fsm.context import FSMContext


client = AsyncOpenAI(api_key=OpenAI_KEY)

router = Router()

async def init_quiz(state: FSMContext):
    await state.update_data(score = 0)


async def get_quiz_question(topic:str)->str:
    responses=await client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {"role":"system", "content":f'Сгенирируй вопрос по теме {topic}'}]
    )
    return responses.choices[0].message.content



async def check_answer(question: str, answer: str) -> str:
    response = await client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    f"Проверь правильность ответа на квиз.\n"
                    f"Вопрос: {question}\n"
                    f"Ответ: {answer}\n"
                    'Скажи только одно слово: "правильно" или "неправильно".'
                ),
            }
        ],

    )
    print(response.choices[0].message.content.strip())
    return response.choices[0].message.content.strip()


async def increase_score(state: FSMContext):
    data = await state.get_data() #{}
    score = data.get('score', 0) + 1
    await state.update_data(score=score)
    return score


async def get_score(state: FSMContext) -> int:
    data = await state.get_data()
    return data.get('score', 0)