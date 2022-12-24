import requests
import json
from loader import dp
from aiogram import types
from decouple import config

BASE_URL = config('BASE_URL')
AUTH_TOKEN = config('TOKEN')


@dp.message_handler()
async def post_url(message: types.Message):
    url = message.text
    head = {'Authorization': 'token {}'.format(AUTH_TOKEN)}
    try:
        response = requests.post(url=f'{BASE_URL}/api/v1/url/', headers=head, data={
            'original_url': url
        })
        if response.status_code != 404:
            await message.reply('URL muvoffaqiyatli yuborildi!')
            data = json.loads(response.content)
            print(data)
        else:
            await message.reply(f"Uzr nimadur xato - {response.status_code}")
    except requests.HTTPError or requests.ConnectionError as er:
        print(er)
