import requests
from loader import dp
from aiogram import types
from decouple import config

BASE_URL = config('BASE_URL')
AUTH_TOKEN = config('TOKEN')


@dp.message_handler()
async def post_url(message: types.Message):
    url = message.text
    print(url)
    head = {'Authorization': 'token {}'.format(AUTH_TOKEN)}
    try:
        response = requests.post(url=f'{BASE_URL}/api/v1/url/', headers=head, data={
            'original_url': url
        })
    except:
        print('Error!')
