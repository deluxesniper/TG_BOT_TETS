from aiogram import Router
from openai import AsyncOpenAI
from handlers.Config.configs import OpenAI_KEY


client = AsyncOpenAI(api_key=OpenAI_KEY)


router=Router()


async def user_translations(languages:str,text:str)->str:
    responses=await client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {"role":"system","content":f"Ты профиссиональный переводчик. Переведи текст {languages}на профисссиональный диалоговый "},
            {"role":"user","content":f"Переведи еще текст{text}"}

        ]
    )
    return  responses.choices[0].message.content