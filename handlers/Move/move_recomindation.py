from aiogram import Router
from openai import AsyncOpenAI
from handlers.Config.configs import OpenAI_KEY


client = AsyncOpenAI(api_key=OpenAI_KEY)


router=Router()


async def recommendations_move(films:str)->str:
    responses=await client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role":"system","content":f" Подскажи мне по 5 фильмов  каждого года,  из жанра{films}  за 2022 по 2024 год  "}
        ]
    )
    return  responses.choices[0].message.content