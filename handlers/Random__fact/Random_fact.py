from http.client import responses
from openai import OpenAI
from handlers.Config.configs import OpenAI_KEY


client=OpenAI(api_key=OpenAI_KEY)


async def random_fact():
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {'role': 'system', 'content': 'Отвечай как самый умный человек на земле'},
            {'role': 'user', 'content': 'Факт как появились краски на земле и где они сначала использовались'}
        ]
    )
    return response.choices[0].message.content

