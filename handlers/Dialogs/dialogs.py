from openai import OpenAI
from handlers.Config.configs import OpenAI_KEY
from handlers.Random__fact.Random_fact import client

client=OpenAI(api_key=OpenAI_KEY)


dialogis={}




PERSONS={
    "Вернер Гейзенберг":" Ты введешь  беседу как Вернер Гейзенберг",
    "Генри Форд":"Ты  рассказываешь про автомобили как Генри Форд",
    "Стив Джобс":"Ты рассказываешь про IT и технику Aplle как Стив Джобс",
}

async def ask_role_gpt(user_id: int, text: str) -> str:
    print(dialogis[user_id])

    if user_id not in dialogis:
        return 'Сначала начни командой /talk'

    dialogis[user_id]['messages'].append({'role': 'user', 'content': text})

    persona = dialogis[user_id]['persona']

    response = await client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {'role': 'system', 'content': f'Ты общаешься как {persona}. Никогда не выходи из этой роли'},
            *dialogis[user_id]['messages']
        ],
        temperature=0.7,
        max_tokens=400
    )

    answer = response.choices[0].message.content

    dialogis[user_id]['messages'].append({'role': 'assistant', 'content': answer})

    return answer